pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'calculator-api:latest' // Имя Docker-образа
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Сборка Docker-образа
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Запуск тестов (если есть)
                    // Пример: sh 'docker run $DOCKER_IMAGE npm test'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Публикация Docker-образа в реестре (например, Docker Hub)
                    // Пример: sh 'docker push $DOCKER_IMAGE'
                    
                    // Разворачивание Docker-контейнера
                    // Пример: sh 'docker run -d -p 5000:5000 --name calculator-api $DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        success {
            echo 'Сборка и развертывание успешно завершены!'
        }

        failure {
            echo 'Сборка и развертывание завершились с ошибкой. Пожалуйста, проверьте логи для получения подробностей.'
        }
    }
}
