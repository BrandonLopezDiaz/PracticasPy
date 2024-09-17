i = lambda x,y : x + y
print(i(3,2))

# Definición de una función lambda que suma dos números
suma = lambda x, y: x + y

# Llamando a la función lambda
resultado = suma(5, 3)
print(resultado)  # Salida: 8

# Usando lambda con sorted para ordenar por el segundo elemento
pares = [(1, 3), (4, 2), (2, 5)]
ordenado = sorted(pares, key=lambda x: x[1])
print(ordenado)  # Salida: [(4, 2), (1, 3), (2, 5)]
