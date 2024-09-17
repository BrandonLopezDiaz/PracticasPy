edades = [20,23,21,32,12,12,12,43]

def eresmayor(edad):
    return edad>=18

#Es un filtro que puede llamar a una funcion y retorna una lista por list
#Para hablar funciones para listas o mas cosas 
entra= list(filter(eresmayor, edades))
print(entra)