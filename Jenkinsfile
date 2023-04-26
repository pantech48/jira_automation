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
                    sh 'ls -la'
                    sh 'pip --version'
                    sh 'python -m venv venv'
                    sh '. ./venv/bin/activate'
                    sh "pip install -r requirements.txt"
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