#Suma de los dígitos de un número:
#Recorre cada dígito de un número (convirtiéndolo en una cadena de texto) y
#suma sus valores utilizando un ciclo for.

numeros = input("ingrese numero: ")
suma_digitos = 0

for digito in (numeros):
    suma_digitos += int(digito)
print(F"la suma de los numeros de {numeros} es {suma_digitos}")

# numero = int(input("pon el numero hasta el que quieres sumar: "))

# contador = 1
# sumar = 0

# for numero in range(numero):
#     contador = numero 
#     sumar += contador
#     print(f"numero: {contador}")
# print(f"la suma total es: {sumar}")



