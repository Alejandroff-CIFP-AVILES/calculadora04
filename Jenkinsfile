pipeline {
	agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }

		stage('Checkout') {
			steps {
				git url: 'https://github.com/Alejandroff-CIFP-AVILES/calculadora04', branch: "main"
			}
		}
		 
		stage("Ejecucion test"){
			steps {
				script {
	         		 sh 'calculadora.py 4 2'
	          		
	          	}
          	}
        }
		stage("Unit test"){
			steps {
				script {
					sh 'test_calculator.py'
				}
			}
		}
	}
}