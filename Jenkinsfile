pipeline {
	agent any
	stages { 
		stage('Checkout') {
			steps {
				git url: 'https://github.com/Alejandroff-CIFP-AVILES/calculadora04', branch: "main"
			}
		}
	
		stage("Ejecucion test"){
			steps {
				script {
	         		 sh """
	          		 calculator.py 4 2
	          		"""
	          	}
          	}
        }

		
		stage("Unit test"){
			steps {
				python3 test_calculator.py
			}
		}
	}
}