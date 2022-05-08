pipeline {
	agent { docker { image 'python:3.10.1-alpine' } }
	stages { 
		stage('Checkout') {
			steps {
				git url: 'https://github.com/Alejandroff-CIFP-AVILES/calculadora04', branch: "main"
			}
		}	
		stage("Ejcucion test"){
			steps {
				sh 'python3 calculator.py 4 2'
			}
		}
		stage("Unit test"){
			steps {
				sh 'python3 test_calculator.py'
			}
		}
	}
}