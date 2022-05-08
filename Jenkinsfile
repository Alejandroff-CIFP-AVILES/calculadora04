pipeline {
	agent any
	stages { 
		stage('Checkout') {
			steps {
				git url: 'https://github.com/Alejandroff-CIFP-AVILES/calculadora04', branch: "main"
			}
		}
		stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
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