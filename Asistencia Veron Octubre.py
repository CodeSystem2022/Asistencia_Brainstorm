# Función descendiente recursiva
def suma_recursiva(num):
    if num >= 1:
        print(num)
        suma_recursiva(num-1)
    elif num < 0:
        print("Valor incorrecto")
regresivo = int(input("Ingrese un número desde donde realizar una cuenta regresiva: "))
suma_recursiva(regresivo)