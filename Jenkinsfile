pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Train Model with MLflow') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python train_model.py'
            }
        }
        stage('View MLflow UI') {
            steps {
                echo 'MLflow UI available at http://localhost:5000'
            }
        }
    }
}
