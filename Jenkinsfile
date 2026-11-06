pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest test_app -v'
            }
        }

        stage('Deploy') {
            steps {
                sh 'mkdir -p /tmp/deploy && cp app.py /tmp/deploy/ && python3 /tmp/deploy/app.py'
            }
        }
    }
}
