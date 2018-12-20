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
        // run tests
        // deploy container
    }
    post {
        always { 
            echo 'I will always say Hello again!'
        }
    }
}
