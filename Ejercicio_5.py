#Tabla de multiplicar de un número:
#Genera la tabla de multiplicar de un número dado del 1 al 10 utilizando un ciclo for.
#Por cada iteración, calcula el producto y muéstralo.

numero = 12

for i in range(1, 11):
    multiplicar = numero * i
    print(F"{numero} x {i} = {multiplicar}")
