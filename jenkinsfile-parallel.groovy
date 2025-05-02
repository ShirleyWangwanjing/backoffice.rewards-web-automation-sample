#!groovy
PROJ_NAME = 'iherb_automation'

CMD_MD_HOME = "mkdir ${BUILD_NUMBER}"

def label = "worker-${UUID.randomUUID().toString()}"
defaultNotification= "wenjing.liu@iherb.com"

timeout(time: 2, unit: 'HOURS') {
    try {
        podTemplate(label: label,
                containers:
                        [containerTemplate(name: 'python', image: 'iherb-docker-local.jfrog.io/cibuildslave/python-selenium:python-selenium', command: 'cat', ttyEnabled: true),
                         containerTemplate(name: 'java', image: 'java:openjdk-8u111-jre-alpine', privileged: false, command: 'cat', ttyEnabled: true)
                        ],
                volumes: [emptyDirVolume(mountPath: '/home/jenkins', memory: true)],
                imagePullSecrets: ['jfrog-authenticate']
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
                                echo("initParameters completed")
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
//        sendEmailNotification()
        error "Build fail, exception: "+exception.message
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
    PROCESSES = "${params.Processes}"
    GOOGLE_CHAT_URL = "${params.GOOGLE_CHAT_URL}"
    echo "...tags="+TAGS

    if (MODEL == "" || MODEL == "null") {
        if (BRANCH_NAME.contains("master")) {
            MODEL = "iHerb.Test.Automation"
        } else {
            MODEL = "iHerb.Test.Automation"
        }
    }
    if (TAGS != "" && TAGS!="null") {
        TAGS= " --tag "+TAGS
    }
    if (ENV == ""||ENV =="null") {
        ENV = "TEST"
    }
    if (PROCESSES == "" || PROCESSES == "null"){
        PROCESSES= "4"
    }
    DIR_MODEL = ""
}


def runBehaveTest(){
   echo "run behave cmd"
    try {
          echo "DIR_MODEL= "+ DIR_MODEL
          behave_cmd = ' python behave_parallel.py '+ TAGS +' --env '+ ENV +' --processes '+ PROCESSES
          echo behave_cmd
          sh behave_cmd
    }catch(e){
        echo "run behave command fail, exception: " + e.message
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
    echo "email service not available for now"
    notificationEmail = "${params.NotificationEmail}"
    echo "notificationEmail="+notificationEmail
    if (notificationEmail == "null") {
        notificationEmail = defaultNotification
    }
    testResult="${currentBuild.currentResult}"
    if ("${currentBuild.currentResult}" != "SUCCESS") {
        emailext subject: "[${currentBuild.currentResult}]Job['${env.JOB_NAME}'] " +
                "[build#${env.BUILD_NUMBER}]",
                to: notificationEmail,
                mimeType: "text/html",
                body: """
                <p>Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]': ${currentBuild.currentResult}</p>
                <p>Check test execution result at &QUOT;
                <a href='${env.BUILD_URL}allure'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>
                  """,
                attachmentsPattern: "artifacts/allure/*.png",
                attachLog: true
    }
}

def sendGoogleChatMessage(){
    testResult="${currentBuild.currentResult}"
    build_url= "${BUILD_URL}"
    googlechatnotification message: 'Automation Test report'+ '\nTest Environment: '+ENV+'\nTest Result: '+"```"+testResult+"```"+'\nTest Report: '+build_url,
            notifyAborted: true, notifyBackToNormal: true, notifyFailure: true, notifyNotBuilt: true, notifySuccess: true, notifyUnstable: true, sameThreadNotification: true, suppressInfoLoggers: true,
            url: GOOGLE_CHAT_URL

}