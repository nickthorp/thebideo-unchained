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
                sh 'build/thebideo-docker-run.sh'
            }
        }
    }
    post {
        always {
            slackNotifier call:"${currentBuild.currentResult}"
            cleanWs()
        }
    }
}
