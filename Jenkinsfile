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
                sh 'which python3 || (apt-get update && apt-get install -y python3 python3-pip)'
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
