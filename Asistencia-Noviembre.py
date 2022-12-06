Asistencia Octubre - Python

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
