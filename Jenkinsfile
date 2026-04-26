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

        stage('Debug Jenkins Docker Runtime') {
            steps {
                script {
                    // #region agent log
                    def debugLog = { hypothesisId, message, data ->
                        def payload = groovy.json.JsonOutput.toJson([
                            sessionId: 'f330b7',
                            runId: 'pre-fix',
                            hypothesisId: hypothesisId,
                            location: 'Jenkinsfile:Debug Jenkins Docker Runtime',
                            message: message,
                            data: data,
                            timestamp: System.currentTimeMillis()
                        ])
                        echo "AGENT_DEBUG ${payload}"
                    }

                    def shellOut = { command ->
                        sh(returnStdout: true, script: "${command} 2>&1 || true").trim()
                    }

                    debugLog('H1', 'Docker CLI lookup', [
                        dockerPath: shellOut('command -v docker'),
                        path: shellOut('printf "%s" "$PATH"')
                    ])
                    debugLog('H2', 'Docker socket and Jenkins user check', [
                        socket: shellOut('ls -l /var/run/docker.sock'),
                        user: shellOut('id')
                    ])
                    debugLog('H3', 'Docker command execution check', [
                        dockerVersion: shellOut('docker --version'),
                        dockerInfo: shellOut('docker info --format "{{.ServerVersion}}"')
                    ])
                    debugLog('H4', 'Docker Compose availability check', [
                        composeVersion: shellOut('docker compose version')
                    ])
                    // #endregion agent log
                }
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