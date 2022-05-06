import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

	def test_multiplicacion(self):
		resultado = calculadora.multiplicacion(2,2)
		self.assertEqual(resultado,4)

if __name__ == '__main__':
	unittest.main()