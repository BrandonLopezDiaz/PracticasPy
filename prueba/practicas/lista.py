# Personas = ["Mart","Ulis","Perez"]
# #El comando del funciona para eliminar un elemento de una lista
# del Personas[0]

# #Remplazar en la lista
# Personas.insert(0, "juan")
# #Agregar en la lista
# Personas.append("Pedro")
# #Elimina al ultimo de la fila igual sirve para extraer el dato de la fila
# i = Personas.pop()

# #con esta forma podemos poner una variable en el mensaje
# print(f'Persona {i}')

# #Tuplas es un arreglo pero cual cual no se puede modificar
# tuple = (11, 'python', True, [1,2,3])
# #Dice donde se encuentra los datos el index
# print(tuple.index(11))
# #El count sirve para saber cuantas veces se repite los elementos
# print(tuple.count(11))
# #Con el len sirve para saber la longitud de las cosas como la tupla
# print(len(tuple))


#conjunto se crea asi para que entienda el programa que es un conjunto no se puedde repetir
#solo muestra una cosa de su tipo
conjunto = set()
conjunto = {1,'pythone','perez',True, True}
#Agregar elemento pero lo pone donde lo quiere 
conjunto.add("Juarez")
#Con esto elimina un dado es especifico del conjunto 
conjunto.discard(True)
#limpiar el conjunto completo 
# conjunto.clear()

#Preguntar si se encuentra cierta informacion en un conjunto 
print ('Juarez' in conjunto) #se encuentra en el conjunto
print ('Juarez' not in conjunto) # No se encuentra
