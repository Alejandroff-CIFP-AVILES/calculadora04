pipeline {
	agent { docker { image 'python:3.7' } }
	stages { 
		stage('Checkout') {
			steps {
				git url: 'https://github.com/Alejandroff-CIFP-AVILES/calculadora04', branch: "main"
			}
		}

		stage('build') {
			steps {
	  			sh 'pip install -r requirements.txt'
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