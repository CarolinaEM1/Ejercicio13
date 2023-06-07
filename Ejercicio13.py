#Hacer un programa para calcular el factorial de un número positivo

numero = int(input("Digite un numero"))

while numero<0:
    print("Error -> digite un numero positivo")
    numero = int(input("Digite un numero"))

factorial = 1

for i in range(1,numero+1):
    factorial *= i

print(f"El factorial del numero {numero} es: {factorial}")

#Carolina EM