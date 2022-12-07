Asistencia Noviembre - Python

#######################################
Alumno/a : Agustina Castro
#######################################

class Persona: # Creamos una clase
    contador_personas = 0 #Variable de clase

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1#incremento
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} = {self.nombre} {self.edad}]'

persona1 = Persona('Ariel', 40)
print(persona1)
persona2 = Persona('Osvaldo', 45)
print(persona2)
persona3 = Persona('Liliana', 34)
print(persona3)
print(f'Valor de contador: {Persona.contador_personas}')

#######################################
Alumno/a : Daniel Dasilva
#######################################

class Vehiculo:
    '''
    Definir una calse padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la calase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y métodos:
    Vehiculo (clase padre)
    -Atributos(Color, ruedas)
    -Metodos(__init__(color, ruedas,) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad (km/hr))
    -Metodos(__init__(Color, ruedas, velocidad) y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Metodos(__init__(Color, ruedas, tipo) y __str__())
    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+', Velocidad(km/hr): '+ str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo


# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# Segundo objeto, pero ahora de la clase Auto
auto = Auto('Amarillo', 4, 120)
print(auto)

# Tercer objeto, el último de la clase Bicilcleta
bici = Bicicleta('Azul', 2, 'Urbana')
print(bici)

#######################################
Alumno/a :Giunta Pilar
#######################################

class Producto:
    contador_producto = 0 #Variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 #Aumento para la variable de clase
        self._id_producto = Producto.contador_productos #Asignación desde la variable de clase
        self._nombre = nombre
        self._precio = precio
    # Métodos setters and getters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio =precio
    #Sobre escribimos el método srt
    def __str__(self):
      return f'Id producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'


    if __name__ == '__main__': #Solo será visible si la prueba se ejecuta desde aqui
        producto1 = Producto('Camiseta', 100.00)
        producto2 = Producto('Pantalon', 150.00)

#######################################
Alumno/a : Octavio Veron
#######################################

class Persona:
    contador_personas = 0

    @classmethod
    def siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} = {self.nombre} {self.edad}]'

persona1 = Persona("Octavio", 21)
print(persona1)
persona2 = Persona("Daniel", 25)
print(persona2)
persona3 = Persona("Carlos", 47)
print(persona3)
Persona.siguiente_valor()
persona4 = Persona("Jose", 28)
print(persona4)
print(f"Valor contador personas: {Persona.contador_personas}")
