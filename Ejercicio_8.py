#Media de una lista de números: Recorre cada elemento de una lista con un ciclo for, acumula su suma y divide entre 
#el número total de elementos para calcular la media.

lista = (1, 5, 10, 14, 22, 44, 55, 62, 78)
suma = 0
contador = 0
for i in lista:
    suma += i 
    contador += 1 
print(F"suma total: {suma}, el tamaño de la lista es: {contador}, la media es: {suma / contador} ")
