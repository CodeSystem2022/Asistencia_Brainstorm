import math # Importamos la clase math para hacer uso de la funcion sqrt(raíz cuadrada)
# Dada la siguinte tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #definimos la tupla
# crear una lista que solo incluya los números menores a 5
# e imprime por consola [1, 3, 2]

lista = [] # Definimos la lista
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio de matematicas para sacar la raíz cuadrada de un número positivo
numero= int(input('Digite un numero positivo: '))
while numero < 0:
    print('error -> Debería ser un número positivo')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')
