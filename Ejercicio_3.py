#Números pares del 1 al 100:
#Usa un ciclo for para recorrer los números del 1 al 100 e imprime solo aquellos
#que sean divisibles entre 2 (números pares).

numero = 1 
limite = 101

for numero in range(1, limite):
    if numero % 2 == 0: #lo uso para saber si es divicible no olvidar 😡 (de nuevo)
        print(numero)
