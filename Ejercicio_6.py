#Verificación de número primo:
#Usa un ciclo for para verificar si un número es divisible por 
#algún número entre 2 y su raíz cuadrada.
#Si no tiene divisores, es primo.

numero = 9
divisores_es_primo = False
raiz_cuadrada = int(numero ** 0.5)

for i in range(3, raiz_cuadrada - 1): 
    if i != numero:
        if numero % i == 0:
            divisores_es_primo = True
            break
if divisores_es_primo:
    print(f"{numero} es un número compuesto.")
else:
    print(f"{numero} es un número primo.")