pipeline {
    agent { dockerfile { dir '.' } }
    stages {
        stage('build') {
            steps {
                sh 'nmap -p5432 10.10.0.5'
            }
        }
    }
}
