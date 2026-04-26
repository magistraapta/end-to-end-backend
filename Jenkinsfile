pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                        -v "$PWD:/app" \
                        -w /app \
                        python:3.12-slim \
                        sh -c "pip install --no-cache-dir uv && UV_PROJECT_ENVIRONMENT=/tmp/venv uv run --frozen pytest"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker compose build backend'
            }
        }

        stage('Deploy Local Containers') {
            when {
                branch 'master'
            }
            steps {
                sh 'docker compose up -d mongodb backend'
            }
        }
    }

    post {
        always {
            sh 'docker compose ps'
        }
    }
}