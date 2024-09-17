lista= [1,2,3,4,5]
lista_2 = [7,8,9]
#Para agregar algun dato mas a la lista con append pero al final de la lista igual el metodo insert pero este al lugar que quieres modificar
lista.append(6)
lista.insert(6, 5)
#El metodo clear limpia todo el arreglo igual existe el pop y el remove como metodo 
# lista.clear()
# lista.pop()
# lista.remove(2)
#Metodo para unir dos listas con elemento
lista.extend(lista_2)
# El count cuenta cuatos elemtos hay en la lista de un elemento en exacto igual podemos poner el index para saber donde esta
#El metodo len para saber la logitud de la lista
print(lista.count(1))
print(lista.index(2))
print(len(lista))
#El reverse da la vuelta de la lista y el soft los ordena
lista.reverse()
lista.sort()
print(lista)