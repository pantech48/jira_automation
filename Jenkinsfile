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
                def pip = sh(script: 'which pip || which pip3', returnStdout: true).trim()
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python main.py'
            }
        }
    }
}