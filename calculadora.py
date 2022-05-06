
import sys
def main():

	print("Calculadora04")
	numero1 = int(sys.argv[1])
	numero2 = int(sys.argv[2])
	print(f"La multiplicacion es: {multiplicacion(numero1, numero2)}.")

def multiplicacion(numero1 , numero2):
	return numero1 * numero2

if __name__ == "__main__":

    main()


