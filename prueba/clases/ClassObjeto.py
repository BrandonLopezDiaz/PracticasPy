class Persona:
    #se incia de esta manera para que pueda decirle las caracterisitcas que tiene.
    def __init__(self, name, lastn, age ):
        self.name = name
        self.lastn = lastn
        self.age = age
        print("Usuarios creado")

    def mostrar(self):
        print (f"la persona se llama: {self.name}")
        print (f"la persona se lastn: {self.lastn}")
        print (f"la persona se age: {self.age}")
    
    #Metodos especiales
    #sirve para eleminar ese  objeto cuando se dice usa
    def __del__(self):
        print(f'Se ha salido el usuario {self.name}')
#instanciar la variable user
user = Persona("Brandon", "Lopez", "20")
#Llamar funciones
user.mostrar()
del(user)

user2 = Persona("Brandon", "Diaz", "21")
user2.mostrar()
