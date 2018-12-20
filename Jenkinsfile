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
                sh './build/convert.sh'
                // package django container
                // run tests
                // deploy container
            }
        }
    }
    post {
        always { 
            echo 'I will always say Hello again!'
        }
    }
}
