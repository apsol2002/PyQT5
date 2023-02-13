# Paso 1. Importar el modulo sqlite3:

import sqlite3

# Paso 2. Crear conexion:

conexion = sqlite3.connect('usuarios.db')

# Paso 3. Crear cursos:

cursor = conexion.cursor()

# Paso 4. Crear una tabla:

sql = '''CREATE TABLE usuario (id INTEGER PRIMARY KEY, email TEXT NOT NULL, clave TEXT NOT NULL)'''
cursor.execute(sql)
conexion.commit()

# Paso 5. Insertar registros

sql = '''INSERT INTO usuario VALUES (1, 'juan@gmail.com', 'ju@n' )'''
cursor.execute(sql)
conexion.commit()

sql = '''INSERT INTO usuario VALUES (2, 'maria@gmail.com', 'm@ri@' )'''
cursor.execute(sql)
conexion.commit()

# Paso 6. Ver los registros.

sql = '''SELECT * FROM usuario'''
cursor.execute(sql)

resultados = cursor.fetchall()

for r in resultados:
    print(r)
