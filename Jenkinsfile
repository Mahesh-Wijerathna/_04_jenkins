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
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python train_model.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Model training completed'
            }
        }
    }
}
