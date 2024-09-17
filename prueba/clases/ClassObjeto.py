class Persona:
    #se incia de esta manera para que pueda decirle las caracterisitcas que tiene.
    #Para encausular usar dos __ ejemplo __name
    def __init__(self, name, lastn, age ):
        self.__name = name
        self.lastn = lastn
        self.age = age
        print("Usuarios creado")

    def mostrar(self):
        print (f"la persona se llama: {self.__name}")
        print (f"la persona se lastn: {self.lastn}")
        print (f"la persona se age: {self.age}")
    
    #Metodos especiales
    #sirve para eleminar ese  objeto cuando se dice usa
    def __del__(self):
        print(f'Se ha salido el usuario {self.__name}')
    #Otra forma de mostrar un mensaje
    def __str__(self) -> str:
        return 'la persona se llama {}, se apellida {} y tiene la edad de {}'.format(self.__name, self.lastn, self.age)
    
    #Caminar 
    def caminar(self, caminando):
        self.camina = caminando
        if (self.camina):
            return 'esta caminando'
        else :
            return 'Detenido'
        
#instanciar la variable user y le envio los datos para que almacene 
user = Persona("Brandon", "Lopez", "20")
#Llamar funciones
user.mostrar()
del(user)

user2 = Persona("Brandon", "Diaz", "21")
user2.__name = "BLDZ"
print(str(user2))
print(user2.caminar(True))
