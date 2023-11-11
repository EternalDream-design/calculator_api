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
        stage('Scanning pythom code semgrep') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv .venv
                source .venv/bin/activate
                pip3 install semgrep
                rm -r calc_api_appsec-scan.xml
                semgrep --config=auto --junit-xml -o reports/calc_api_appsec-scan.xml calc_api_appsec.py
                deactivate'''
                junit skipMarkingBuildUnstable: true, testResults: 'reports/calc_api_appsec-scan.xml'
            }
        }
        stage('Build docker-container'){
            steps{
                script{
                    sh 'docker build -f Dockerfile -t calc_api_appsec .'
                }
            }
          }
         stage('Scanning lib and containers trivy'){
            steps {
                sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl'
                sh 'mkdir -p reports'
                sh 'rm -r calc_api_appsec-scan.html'
                sh 'trivy image --ignore-unfixed --format template --template "@html.tpl" -o reports/calc_api_appsec-scan.html calc_api_appsec:latest'
                publishHTML target : [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'api_calc-scan.html',
                    reportName: 'Trivy Scan',
                    reportTitles: 'Trivy Scan'
                ]

                // Scan again and fail on CRITICAL vulns
                sh 'trivy image --ignore-unfixed --vuln-type os,library --exit-code 1 --severity CRITICAL calc_api_appsec:latest'
              }
            }
           stage('Run docker-container'){
            steps{
                script{
                    sh 'docker run -d -p 5000:5000 calc_api_appsec:latest'
                		}
            		}
        	}
     }
 }
