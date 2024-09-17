#Clase padre
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        print("Persona creada")

    def imprimir(self):
        return 'Persona llamada: {}, Edad de : {}, Con el sexo: {}'.format(self.nombre, self.edad, self.sexo)

persona = Persona("Juan", "20", "H")
print(persona.imprimir())

#Empleado
#asi se debe que herredar las clases juntos a sus metodos y la multi herencia es solo darle las clases que va a usar el hijo para tener sus metodos y atricutos ejemplo modulo3(modulo1,modulo2)
class Empleado(Persona):

    def datosEmpleado(self, salario, vacaciones):
        print(f"El salario es de {salario}")
        print(f"Dias de vacaciones son de {vacaciones}")


empleados = Empleado("Juan", "20", "H")
empleados.imprimir()
empleados.datosEmpleado(3000, 20)