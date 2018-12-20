pipeline {
    agent any
    stages {
        stage('Checkout') {
            checkout scm
        }
        stage('Convert') {
            steps {
                sh './build/convert.sh'
                // package django container
                // run tests
                // deploy container
                // 
            }
        }
    }
}
