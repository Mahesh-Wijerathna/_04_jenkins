pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Setup Python') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Train Model') {
            steps {
                sh './venv/bin/python train_model.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Model training completed'
            }
        }
    }
}
