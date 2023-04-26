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
        stage('Build') {
            agent {
                docker { image 'python:3' }
            }
        }
        stage('Install Dependencies') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
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