# miCursos =["PYTHON", "Mysql", "Rubi"]
# print(miCursos)
# name =["Juan", "Perez", "Rubi"]
# for i in name:
#         print(f'Su nombres es {i}')
# divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# reponse = input("Ingrese una divisa: ")
# if reponse in divisas :
#         print(f"La divisa es valida: {divisas[reponse]}")
# else:
#         print(f'Esa divisa no existe{reponse}')

# tupla = (10, 2.1, "Hola", [12,12,33])
# print(f"La tupla es: {tupla}")

# def saludo():
#     return print("Hola a todos")
# saludo()
# def holaTal(nombre):
#     return print(f"¡Hola {nombre}")
# holaTal("Juan")
# def usuario ():
#     name = input("Ingrese su nombre")
#     edad= input("Ingrese su edad")
#     return print(f"Hola {name} tu edad es {edad}")
# usuario() 
# def requerid(op1, op2):
#     result = op1 + op2
#     return print(result)
# requerid(1+20)

# def error():
#     try:
#         return 10/0
#     except ZeroDivisionError:
#         return print("En la operacion hubo un cero")

# def listaerror():
#     try:
#         miLista = [1,2,3,4,5]
#         return miLista[7]
#     except Exception as e:
#         print(f"{type(c).__name__} + hubo un error el cual se debe que esta buscando un numero que no existe en la cadena")



# class Persona:
#     def __init__(self, nombre, edad, sexo, nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.sexo = sexo
#         self.nacionalidad = nacionalidad
#         print("Persona creada")

#     def imprimir(self):
#         return 'Persona llamada: {}, Edad de : {}, Con el sexo: {} y la nacionalidad: {}'.format(self.nombre, self.edad, self.sexo, self.nacionalidad)

# persona = Persona("Juan", "20", "H", "Mexicana")
# print(persona.imprimir())

# class Auto:
#     def __init__(self,marca, modelo, año, color):
#         self.__marca = marca
#         self.__modelo = modelo
#         self.__año = año
#         self.__color = color
#         print("Auto creado")

#     def detalles(self):
#         return 'Auto: {}, del modelo : {}, del año: {} y color: {}'.format(self.__marca, self.__modelo, self.__año, self.__color)
#     def estadoC(self, estado):
#         self.estadoCarro = estado
#         if (self.estadoCarro):
#             print("El carro esta {} esta prendido".format(self.__marca))
#         else:
#             print("El carro de la marca {} esta apagado".format(self.__marca))

# Carro = Auto("Nissan", "T200", "2001", "Rojo")
# print(Carro.detalles())
# Carro.estadoC(True)