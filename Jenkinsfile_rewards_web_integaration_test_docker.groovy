#!groovy
PROJ_NAME = 'rewards_mgr_auto_ui'

CMD_MD_HOME = "mkdir ${BUILD_NUMBER}"

def label = "worker-${UUID.randomUUID().toString()}"
defaultNotification= "wenjing.liu@iherb.com"
notificationResult="FAILURE"

failing_list = ""

timeout(time: 3, unit: 'HOURS') {
    try {

            node() {
                try{

                        stage('Preparation') {
                            sh "docker build -q -f /opt/Dockerfile -t python0.1:latest ."
                            sh "docker run --name python python0.1"
                            checkoutCode()
                        }
                        def envVars = ["AUTOMATION_DOCKER_ENV=automation_docker_env "]
                        withEnv(envVars){
                            stage('Integration_Test') {
                                initParameters()
                                runBehaveTest()
                            }
                        }


                }finally{

                        stage("PublishReport") {
                            publishReport()
                        }
                        stage('SendNotification'){
                            echo ".....readFileLineByLine()"
                            readFileLineByLine()
                            sendGoogleChatMessage()

                        }
                    }

            }


    }catch(exception)
    {
        //sendEmailNotification()
        error "Build fail, please read log"
    }finally{
    }

}


def clearUp(){
    echo "Start to do clear up"
    echo "PROJ_NAME="+PROJ_NAME
    if (isUnix()) {
        echo "in unix"
        sh 'rm -rf ' + PROJ_NAME
        sh 'cp -r /tmp/.store.force ../artifacts'
        sh 'chmod -R o+xw artifacts/allure'
    } else {
        echo " not unix"
        bat(
                returnStatus: true,
                script: 'RD /Q /S ' + PROJ_NAME
        )
        bat(
                returnStatus: true,
                script: 'robocopy %temp%/.store.force ../artifacts *.yml /S'
        )
    }
}

def checkoutCode(){
    echo 'Create directory with project name'

    if (isUnix()) {
        sh CMD_MD_HOME
    } else {
        bat(CMD_MD_HOME)
        bat('DIR /s /b')
    }

    BRANCH_NAME = "${params.GIT_BRANCH}"
    echo "BRANCH_NAME="+BRANCH_NAME
    if (BRANCH_NAME == "null") {
        BRANCH_NAME = "${env.BRANCH_NAME}"
    }
    echo "Checkout source code from " + BRANCH_NAME
    checkout scm
}

def initParameters(){
    MODEL = "${params.Model}"
    ENV = "${params.Env}"
    TAGS = "${params.Tags}"
    GOOGLE_CHAT_URL = "${params.GOOGLE_CHAT_URL}"
    echo "...tags="+TAGS
    if (MODEL == "null") {
        if (BRANCH_NAME.contains("master")) {
            MODEL = ""
        } else {
            MODEL = ""
        }
    }

    if (ENV == "null") {
        ENV = "test"
    }

    if (TAGS == "null") {
        TAGS= ""
    }

    echo "TAGS="+TAGS
    DIR_MODEL = ""
}


def runBehaveTest(){
    try {
        echo "DIR_MODEL= "+ DIR_MODEL
        dir(DIR_MODEL) {
            echo "in dir_model"
            BEHAVE_ARGS = "--logging-level DEBUG --no-capture " +
                    "-f allure_behave.formatter:AllureFormatter " +
                    "-o artifacts/allure " +
                    "-f rerun " +
                    "-o failing.features " +
                    "--junit --junit-directory artifacts/junit " +
                    TAGS +
                    " -k -D browser=chrome -D env=" + ENV

            BEHAVE_ARGS_RERUN = "--logging-level DEBUG --no-capture " +
                    "-f allure_behave.formatter:AllureFormatter " +
                    "-o artifacts/allure " +
                    "@failing.features " +
                    " -k -D browser=chrome -D env=" + ENV

            if (isUnix()) {
                echo "is unix...."
                echo "build result................................"+"${currentBuild.currentResult}"
                try{
                    echo "run command: python -m behave " + BEHAVE_ARGS
                    sh "python -m behave " + BEHAVE_ARGS
                    notificationResult="SUCCESS"
                    echo "notification success"
                    echo "@_@ First round test success! "
                }
                catch( exception1){
                    echo "@_@ First round test fail! "
                    echo "First round result:"+"${currentBuild.currentResult}"
                    try{
                         echo "second run command: python -m behave " + BEHAVE_ARGS_RERUN
                         sh "python -m behave " + BEHAVE_ARGS_RERUN
                         echo "@_@ Second round test succeed"
                         notificationResult="RERUN THEN SUCCESS"
                         echo "notification rerun and success"
                    }
                    catch(exception2){
                        echo "@_@ Second round test fail"
                        notificationResult="UNSTABLE"
                        echo "notification unstable"
                    }
                }
                finally{
                    echo "finally result:"+"${currentBuild.currentResult}"
                    echo "@_@ All test cases finished! "
                }

            } else {
                echo "python -m behave " +
                        BEHAVE_ARGS
                bat(
                        returnStatus: true,
                        script: "..\\PythonInstallation\\Scripts\\python.exe -m behave " +
                                BEHAVE_ARGS
                )
                echo " Run behave command in else mode finished"
            }

        }
    }
    finally {
        clearUp()
    }
}

def publishReport(){
        echo "publish report, result: "+"${currentBuild.currentResult}"
        result_before_publish_report =  "${currentBuild.result}"
        echo "publish report, result: "+result_before_publish_report
        archiveArtifacts artifacts: 'artifacts/allure/*.json'
        junit testResults: 'artifacts/junit/*.xml'
        allure jdk: '', report: "${PROJ_NAME}", results: [[path: 'artifacts/allure']]
        echo ".....after publish report"
        //currentBuild.result = 'SUCCESS'
        echo "...111 after publish report, result: "+"${currentBuild.result}"
        echo "....222 after publish report, result: "+"${currentBuild.currentResult}"
}

//def setBuildResult(){
//    echo "publish report 222................................"+"${currentBuild.currentResult}"
//    //currentBuild.currentResult = 'SUCCESS'
//    post {
//         success {
//             echo "test post"
//             echo "${env.BUILD_URL} has result success"
//             echo "post complete"
//         }
//     }
//    echo "publish report 333................................"+"${currentBuild.currentResult}"
//}

def readFileLineByLine() {
    echo ".............readFileLineByLine"
    def exists = fileExists 'failing_case_list.txt'
    if (exists){
        echo ".............exists"
        def file_content =  readFile "failing_case_list.txt"
        failing_list= file_content
        echo ".............failing_list="+failing_list
//        test = file.split("\n")
        echo ".............complete readFileLineByLine"
    }

}

//def sendEmailNotification() {
//    notificationEmail = "${params.NotificationEmail}"
//    echo "notificationEmail="+notificationEmail
//    if (notificationEmail == "Null") {
//        notificationEmail = defaultNotification
//    }
//    testResult="${currentBuild.currentResult}"
//    echo "testResult}="+testResult
//    if ("${currentBuild.currentResult}" != "SUCCESS") {
//         emailext body: '''${SCRIPT, template="allure-report.groovy"}''',
//            subject: "[Jenkins] Rewards Manager Automation Execution Summary",
//            to: notificationEmail,
//                attachmentsPattern: "artifacts/allure/*.png",
//                attachLog: true
//    }
//}

def sendGoogleChatMessage(){
    testResult="${currentBuild.currentResult}"
    build_url= "${BUILD_URL}"
    echo "failing_list in result......="+failing_list
    if (failing_list != ""){
        failing_notification = '\nFailing Case List:\n'+ failing_list
    }else{
        failing_notification = ''
    }

    googlechatnotification message: 'Automation Test report'+ '\nTest Environment: '+ENV+'\nTest Result: '+"```"+notificationResult+"```"+'\nTest Allure Report:\n '+build_url+'allure'+failing_notification,
            notifyAborted: true, notifyBackToNormal: true, notifyFailure: true, notifyNotBuilt: true, notifySuccess: true, notifyUnstable: true, sameThreadNotification: true, suppressInfoLoggers: true,
            url: GOOGLE_CHAT_URL
}