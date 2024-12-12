#Cantidad de dígitos de un número: Usa un ciclo for para recorrer los caracteres de un número convertido 
#a cadena de texto y cuenta cuántos tiene.

numero = "1006"
contador = 0

for i in numero: 
     contador += 1
     print(F"cuenta de caracteres es: {i}")
print(F"el tamaño es: {contador}")