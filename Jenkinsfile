pipeline {
    agent any
    
    stages{
        stage('Clear old repo and Git clone new repo'){
            steps{
                script{
                    sh 'rm -rf Api_calc_appsec'
                    sh 'git clone https://github.com/EternalDream-design/calculator_api.git && cd calculator_api'
                }
            }
        }
        stage('Clear'){
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
                    sh 'docker build -f Dockerfile -t api_calc .'
                    sh 'docker run -d -p 5000:5000 api_calc:latest'
                }
            }
        }
    }
}
