pipeline {
	agent any
	stages { 
		stage('Checkout') {
			steps {
				git url: 'https://github.com/Alejandroff-CIFP-AVILES/calculadora04', branch: "main"
			}
		}	
		stage("Ejcucion test"){
			steps {
				python3 calculator.py 4 2
			}
		}
		stage("Unit test"){
			steps {
				python3 test_calculator.py
			}
		}
	}
}