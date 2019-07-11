pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Convert') {
            steps {
                sh 'chmod 755 build/*.sh'
                sh 'build/convert.sh'
                
            }
        }
        stage('Package') {
            steps {
                sh 'build/thebideo-docker.sh'
            }
        }
        
        stage('Deploy') {
            steps {
                withCredentials([usernameColonPassword(credentialsId: '1a5f4c2f-9662-415c-9e26-58b6840b2d49', variable: 'CREDS')]) {
                    base64 = CREDS.bytes.encodeBase64().toString()
                    httpRequest consoleLogResponseBody: true, contentType: 'APPLICATION_JSON', customHeaders: [[maskValue: false, name: 'Authorization', value: "Basic ${base64}"]], httpMode: 'POST', ignoreSslErrors: true, responseHandle: 'NONE', timeout: 30, url: 'http://192.168.0.25/api/v2/job_templates/7/launch/', validResponseCodes: '201'
                }
            }
        }
        
    }
    post {
        always {
            slackBOOM "${currentBuild.currentResult}"
            cleanWs()
        }
    }
}
