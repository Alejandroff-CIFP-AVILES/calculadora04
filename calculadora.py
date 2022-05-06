

def main():
	print("Calculadora04")
	numero1 = int(input("Dígame el primer número: "))
	numero2 = int(input(f"Dígame el primer número: "))
	print(f"La multiplicacion es: {multiplicacion(numero1, numero2)}.")

def multiplicacion(numero1 , numero2):
	return numero1 * numero2

if __name__ == "__main__":
    main()

