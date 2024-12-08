#Factorial de un número dado: Encuentra el factorial de un número multiplicando todos los números desde 1 
#hasta ese número con un ciclo for. 
#Asegúrate de inicializar la variable acumuladora en 1. solicitar el numero
numero = int(input("ingrese un numero para calcular "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i
    print(f"el resultado de {numero} es {factorial} ")