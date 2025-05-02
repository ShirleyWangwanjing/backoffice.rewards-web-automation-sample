#!groovy
PROJ_NAME = 'rewards_mgr_auto_ui'

CMD_MD_HOME = "mkdir ${BUILD_NUMBER}"

def label = "worker-${UUID.randomUUID().toString()}"
defaultNotification= "wenjing.liu@iherb.com"

timeout(time: 2, unit: 'HOURS') {
    try {
        podTemplate(label: label,
                containers:
                        [containerTemplate(name: 'python', image: 'reg.iherb.net/cibuildslave/python-selenium:python-selenium-new', command: 'cat', ttyEnabled: true),
                         containerTemplate(name: 'java', image: 'java:openjdk-8u111-jre-alpine', privileged: false, command: 'cat', ttyEnabled: true)
                        ],
                volumes: [emptyDirVolume(mountPath: '/home/jenkins', memory: true)],
                imagePullSecrets: ['harbor-authenticate']
        ) {
            node(label) {
                try{
                    container('python') {
                        stage('Preparation') {
                            checkoutCode()
                        }
                        def envVars = ["AUTOMATION_DOCKER_ENV=automation_docker_env "]
                        withEnv(envVars){
                            stage('Integration_Test') {
                                initParameters()
                                runBehaveTest()
                            }
                        }

                    }
                }finally{
                    container('java') {
                        stage("PublishReport") {
                            publishReport()
                        }
                    }
                    sendGoogleChatMessage()
                }
            }
        }
    }catch( exception)
    {
        sendEmailNotification()
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
                    "--junit --junit-directory artifacts/junit " +
                    TAGS +
                    " -k -D browser=chrome -D env=" + ENV

            if (isUnix()) {
                echo "python -m behave " + BEHAVE_ARGS
                sh "python -m behave " + BEHAVE_ARGS
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
    archiveArtifacts artifacts: 'artifacts/allure/*.yaml'
    junit testResults: 'artifacts/junit/*.xml'
    allure jdk: '', report: "${PROJ_NAME}", results: [[path: 'artifacts/allure']]
}

def sendEmailNotification() {
    notificationEmail = "${params.NotificationEmail}"
    echo "notificationEmail="+notificationEmail
    if (notificationEmail == "Null") {
        notificationEmail = defaultNotification
    }
    testResult="${currentBuild.currentResult}"
    echo "testResult}="+testResult
    if ("${currentBuild.currentResult}" != "SUCCESS") {
         emailext body: '''${SCRIPT, template="allure-report.groovy"}''',
            subject: "[Jenkins] Rewards Manager Automation Execution Summary",
            to: notificationEmail,
                attachmentsPattern: "artifacts/allure/*.png",
                attachLog: true
    }
}
def sendGoogleChatMessage(){
    testResult="${currentBuild.currentResult}"
    build_url= "${BUILD_URL}"
    googlechatnotification message: 'Automation Test report'+ '\nTest Environment: '+ENV+'\nTrigger by: '+committer+':'+branch+'\nTest Result: '+"```"+testResult+"```"+'\nTest Report: '+build_url+'\nTest Allure Report: '+build_url+'allure'+'\nArtifacts: '+build_url+'artifact/allure-report.zip',
            notifyAborted: true, notifyBackToNormal: true, notifyFailure: true, notifyNotBuilt: true, notifySuccess: true, notifyUnstable: true, sameThreadNotification: true, suppressInfoLoggers: true,
            url: GOOGLE_CHAT_URL

}