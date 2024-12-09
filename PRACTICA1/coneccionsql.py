import sqlite3

# Función para conectarse a la base de datos
def conectar_bd(nombre_bd):
    try:
        conexion = sqlite3.connect(nombre_bd)
        print("Conexión exitosa a la base de datos")
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Función para insertar datos en la tabla Departamento
def insertar_departamento(conexion, df_departamento):
    try:
        df_departamento.to_sql('Departamento', conexion, if_exists='replace', index=False)
        print("Datos insertados en la tabla Departamento")
    except Exception as e:
        print(f"Error al insertar datos en la tabla Departamento: {e}")

# Función para insertar datos en la tabla Municipio
def insertar_municipio(conexion, df_municipio):
    try:
        df_municipio.to_sql('Municipio', conexion, if_exists='replace', index=False)
        print("Datos insertados en la tabla Municipio")
    except Exception as e:
        print(f"Error al insertar datos en la tabla Municipio: {e}")

# Función para insertar datos en la tabla DatosCovid
def insertar_datos_covid(conexion, df_datos_covid):
    try:
        df_datos_covid.to_sql('DatosCovid', conexion, if_exists='replace', index=False)
        print("Datos insertados en la tabla DatosCovid")
    except Exception as e:
        print(f"Error al insertar datos en la tabla DatosCovid: {e}")
