#Verificación de número primo:
# Usa un ciclo for para verificar si un número es divisible por 
# algún número entre 2 y su raíz cuadrada.
# Si no tiene divisores, es primo.

numero = 13
divisores_es_primo = True
raiz_cuadrada = 1

for i in range(2, raiz_cuadrada + 1):
    if numero % i == 0:
        divisores_es_primo = False
        break
if divisores_es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")