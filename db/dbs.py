import sqlite3

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect("MiBase.DB")

# Crear la tabla USUARIOS si no existe
def crear_tabla():
    conexion = conectar()
    curso = conexion.cursor()
    curso.execute('''
        CREATE TABLE IF NOT EXISTS USUARIOS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            EDAD INTEGER,
            SEXO VARCHAR(50)
        )
    ''')
    conexion.commit()
    conexion.close()

# Función para crear (insertar) un nuevo usuario
def crear_usuario(nombre, edad, sexo):
    conexion = conectar()
    curso = conexion.cursor()
    curso.execute("INSERT INTO USUARIOS (NOMBRE, EDAD, SEXO) VALUES (?, ?, ?)", (nombre, edad, sexo))
    conexion.commit()
    conexion.close()

# Función para leer (obtener) todos los usuarios
def obtener_usuarios():
    conexion = conectar()
    curso = conexion.cursor()
    curso.execute("SELECT * FROM USUARIOS")
    usuarios = curso.fetchall()
    conexion.close()
    return usuarios

# Función para leer (obtener) un usuario por ID
def obtener_usuario_por_id(usuario_id):
    conexion = conectar()
    curso = conexion.cursor()
    curso.execute("SELECT * FROM USUARIOS WHERE id = ?", (usuario_id,))
    usuario = curso.fetchone()
    conexion.close()
    return usuario

# Función para actualizar un usuario por ID
def actualizar_usuario(usuario_id, nombre, edad, sexo):
    conexion = conectar()
    curso = conexion.cursor()
    curso.execute("UPDATE USUARIOS SET NOMBRE = ?, EDAD = ?, SEXO = ? WHERE id = ?", (nombre, edad, sexo, usuario_id))
    conexion.commit()
    conexion.close()

# Función para eliminar un usuario por ID
def eliminar_usuario(usuario_id):
    conexion = conectar()
    curso = conexion.cursor()
    curso.execute("DELETE FROM USUARIOS WHERE id = ?", (usuario_id,))
    conexion.commit()
    conexion.close()

# Crear la tabla si no existe
crear_tabla()

# Crear algunos usuarios
crear_usuario('Carlos', 30, 'Masculino')
crear_usuario('Ana', 25, 'Femenino')
crear_usuario('Luis', 40, 'Masculino')

# Leer y mostrar todos los usuarios
print("Usuarios después de la creación:")
usuarios = obtener_usuarios()
print(usuarios)

# Leer un usuario por ID
print("Obtener usuario con ID 1:")
usuario = obtener_usuario_por_id(1)
print(usuario)

# Actualizar el usuario con ID 2
actualizar_usuario(2, 'Ana Maria', 26, 'Femenino')

# Leer y mostrar todos los usuarios después de la actualización
print("Usuarios después de la actualización:")
usuarios = obtener_usuarios()
print(usuarios)

# Eliminar el usuario con ID 3
eliminar_usuario(3)

# Leer y mostrar todos los usuarios después de la eliminación
print("Usuarios después de la eliminación:")
usuarios = obtener_usuarios()
print(usuarios)
