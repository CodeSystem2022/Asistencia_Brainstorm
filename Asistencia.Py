Asistencia Octubre - Python

#######################################
Alumno/a : Agustina Castro
#######################################

class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad,
    con un mètodo calcular_volumen que tendrà la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Digite el ancho del cubo: "))
altura = int(input("Digite la altura del cubo: "))
profundidad = int(input("Digite la profundidad del cubo: "))

cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")

#######################################

Asistencia Octubre - Python

#######################################
Alumno/a: Giunta Pilar
#######################################

class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tenér 2 atributos: altura y base
    el nombre del método será calcular_area utilizando la formula: area = base * altura.
    Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres

    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = int(input('Digite el número para la base del rectangulo: '))
altura = int(input('Digite el número para la altura del rectangulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')

#########################################

