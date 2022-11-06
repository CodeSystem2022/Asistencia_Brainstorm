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

Asistencia Octubre - Python

#######################################
Alumno/a: Jimena Mansilla
#######################################
class Vehiculo:
    '''
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase
    pdre debe tener los siguientes atributos y métodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Métodos(__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad (km/hr))
    -Métodos (__init__(color, ruedas, velocidad) y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña,etc.)
    -Métodos(__init__(color, ruedas, tipo) y __str__()

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: '+self.color+', Ruedas: '+str(self.ruedas)


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad(km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo ' + self.tipo


# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)

# Segundo objeto, pero ahora de la clase Auto
auto = Auto('Blanco', 4, 100)
print(auto)

# Tercer objeto, pero de la clase Bicicleta
bici = Bicicleta('Negro', 2, 'Montaña')
print(bici)
#######################################
