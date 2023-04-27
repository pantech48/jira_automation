pipeline {
    agent any
    triggers {
        cron('H 0 * * *') // This line sets the daily trigger at midnight
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
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python --version'
                    sh "pip install -r requirements.txt"
                    sh 'python main.py'
                    archiveArtifacts artifacts: 'report.xlsx', fingerprint: true
                }
            }
        }
    }
}