pipeline {
    agent any
    
    stages{
    	stage('Clonning new repositorie'){
            steps{
                script{
                    sh 'rm -rf calculator_api'
                    sh 'git clone https://github.com/EternalDream-design/calculator_api && cd calculator_api'
                }
            }
        }
        stage('Clear past Docker'){
            steps{
                script{
                    sh 'docker stop $(docker ps -qa) 2>/dev/null'
                    sh 'docker rm $(docker ps -qa) 2>/dev/null'
                    sh 'docker rmi $(docker images -q) 2>/dev/null'
                }
            }
        }
        stage('Build and run docker-container'){
            steps{
                script{
                    sh 'docker build -f Dockerfile -t calc_api_appsec .'
                    sh 'docker run -d -p 5000:5000 calc_api_appsec:latest'
                }
            }
        }
    }
}
