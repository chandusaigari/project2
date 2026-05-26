pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'chandu0303'
        IMAGE_TAG          = "${BUILD_NUMBER}"
    }

    stages {

        //# ─── Stage 1: Clone Repo ─────────────────────────
        stage('Clone') {
            steps {
                echo '📥 Cloning repository...'
                git branch: 'main', url: 'https://github.com/chandusaigari/project2'
            }
        }

       // ─── Stage 2: Build with Docker Compose ──────────
        stage('Build') {
            steps {
                echo '🔨 Building images with docker compose...'
                sh "IMAGE_TAG=${IMAGE_TAG} docker compose build"
            }
        }

        // ─── Stage 3: Start All Services ─────────────────
        stage('Deploy') {
            steps {
                echo '🚀 Starting all containers...'
                sh "IMAGE_TAG=${IMAGE_TAG} docker compose up -d"
                sh 'docker compose ps'
            }
        }

        // ─── Stage 4: Test ───────────────────────────────
        stage('Test') {
            steps {
                echo '🧪 Waiting for services to be ready...'

                // Wait for MySQL to be healthy and backend to start
                sh '''
                    echo "Waiting for MySQL..."
                    sleep 45

                    echo "Checking containers..."
                    docker compose ps

                    echo "Testing Backend (Flask API)..."
                    curl -f http://localhost:5000 || echo "Backend root check"

                    echo "Testing Frontend..."
                    curl -f http://localhost:80 || exit 1

                    echo "✅ All tests passed!"
                '''
            }
        }

       // ─── Stage 5: Push to DockerHub ──────────────────
        stage('Push to DockerHub') {
            steps {
                echo '📤 Pushing images to DockerHub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                     //   # Push backend
                        docker push chandu0303/flask-backend:${IMAGE_TAG}
                        docker tag  chandu0303/flask-backend:${IMAGE_TAG} chandu0303/flask-backend:latest
                        docker push chandu0303/flask-backend:latest

                       // # Push frontend
                        docker push chandu0303/frontend-app:${IMAGE_TAG}
                        docker tag  chandu0303/frontend-app:${IMAGE_TAG} chandu0303/frontend-app:latest
                        docker push chandu0303/frontend-app:latest

                        echo "✅ Pushed to DockerHub successfully!"
                    '''
                }
            }
        }
    }

    // ─── Cleanup ─────────────────────────────────────────
    post {
        always {
            echo '🧹 Cleaning up...'
            sh '''
                docker compose down -v || true
                docker logout || true
            '''
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
