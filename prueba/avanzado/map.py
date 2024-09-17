def doblar(numero):
    return numero* 2

numeros = [2,32,321,11,9]
#sirve para que el arreglo cada iteracion depende de la pocion
#esto puede servir si necesitamos pasar por cada parte del arreglo sin entrar en un bucle auto incrementable
i = map(doblar, numeros)
x = map(lambda x: x*2, numeros)
print(list(i), list(x))