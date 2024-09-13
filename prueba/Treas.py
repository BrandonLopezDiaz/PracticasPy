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

def error():
    try:
        return 10/0
    except ZeroDivisionError:
        return print("En la operacion hubo un cero")

def listaerror():
    try:
        miLista = [1,2,3,4,5]
        return miLista[7]
    except Exception as e:
        print(f"{type(c).__name__} + hubo un error el cual se debe que esta buscando un numero que no existe en la cadena")