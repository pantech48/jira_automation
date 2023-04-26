pipeline {
    agent {
        docker { image 'python:3' }
    }
    triggers {
        cron('0 0 * * *') // This line sets the daily trigger at midnight
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip --version'
                    sh "pip install --user -r requirements.txt"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'python main.py'
            }
        }
    }
}