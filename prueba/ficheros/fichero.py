from io import open
#Igual existe r que es para leer
fichero =  open('archivo.txt', 'w')
texto = "Hola pipollos"
fichero.write(texto)
fichero.close()