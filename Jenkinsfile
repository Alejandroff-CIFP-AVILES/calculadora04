pipeline {
	agent any
	stages { 
		stage('Checkout') {
			steps {
				git url: 'https://github.com/Alejandroff-CIFP-AVILES/calculadora04', branch: "main"
			}
		}	
		stage("Unit test"){
			steps {
				sh "python3 test_calculator.py"
			}
		}
	}
}