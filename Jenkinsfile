pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Project Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'test -f README.md'
                sh 'test -f experiment10/stock_average.py'
                sh 'test -f experiment11/churn_prediction.py'
                echo 'All project files checked successfully!'
            }
        }
    }
}
