pipeline {
    agent any
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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
            // This is where you would run any tests
            }
        }
        stage('Deploy') {
            steps {
                sh 'python main.py'
            }
        }
    }
}