#Calcula la suma de los números desde 1 hasta n utilizando un ciclo for. Itera sobre 
# los números en el rango de 1 a n y acumula su suma.

limite = int(input("ingrese numero: "))   
suma = 0

for i in range (1, limite):
    print (f"Dato actual: {i}")
    suma += i
    print(f"La suma total de los numeros es: {suma}")

 
