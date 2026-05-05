pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/2024tm93539-dev/ACEest-fitness'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-fitness:v1 .'
            }
        }
    }
}
