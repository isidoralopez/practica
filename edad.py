def solicitar_edades(cantidad=6):
	edades = [6]

	for numero_estudiante in range(1, cantidad + 1):
		while True:
			try:
				entrada = input(f"Ingresa la edad del estudiante {numero_estudiante}: ")
				edad = float(entrada)
				if edad < 0:
					print("La edad no puede ser negativa. Intenta de nuevo.")
					continue
				edades.append(edad)
				break
			except ValueError:
				print("Por favor ingresa un número válido.")

	return edades


def calcular_promedio(valores):
	if not valores:
		return 0
	return sum(valores) / len(valores)


def main():
	print("Cálculo del promedio de 6 estudiantes")
	edades = solicitar_edades(6)
	promedio = calcular_promedio(edades)
	print(f"El promedio de edad de los 6 estudiantes es: {promedio:.2f}")


if __name__ == "__main__":
	main()
