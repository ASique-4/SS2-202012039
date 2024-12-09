import sqlite3
import pandas as pd

# Función para conectarse a la base de datos
def conectar_bd(nombre_bd):
    try:
        conexion = sqlite3.connect(nombre_bd)
        print("Conexión exitosa a la base de datos")
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Función para insertar datos en bloques de 50 registros
def insertar_en_bloques(conexion, df, tabla):
    exitosos = 0
    fallidos = 0
    fallidos_indices = []

    for i in range(0, len(df), 50):
        try:
            df.iloc[i:i+50].to_sql(tabla, conexion, if_exists='append', index=False)
            exitosos += 1
        except Exception as e:
            print(f"Error al insertar bloque {i//50 + 1} en la tabla {tabla}: {e}")
            fallidos += 1
            fallidos_indices.append((i, i+50))

    # Reintentar transacciones fallidas
    for start, end in fallidos_indices:
        try:
            df.iloc[start:end].to_sql(tabla, conexion, if_exists='append', index=False)
            exitosos += 1
            fallidos -= 1
        except Exception as e:
            print(f"Error al reintentar bloque {start//50 + 1} en la tabla {tabla}: {e}")

    print(f"Reporte de inserción para la tabla {tabla}:")
    print(f"Bloques insertados con éxito: {exitosos}")
    print(f"Bloques fallidos: {fallidos}")

# Función para insertar datos en la tabla Departamento
def insertar_departamento(conexion, df_departamento):
    insertar_en_bloques(conexion, df_departamento, 'Departamento')

# Función para insertar datos en la tabla Municipio
def insertar_municipio(conexion, df_municipio):
    insertar_en_bloques(conexion, df_municipio, 'Municipio')

# Función para insertar datos en la tabla DatosCovid
def insertar_datos_covid(conexion, df_datos_covid):
    insertar_en_bloques(conexion, df_datos_covid, 'DatosCovid')