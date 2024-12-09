import pandas as pd
import coneccionsql as con


# INSERTAR DATOS
# Local = Municipios
# Remoto = Global
dfLocal = pd.read_csv('municipio.csv')

# ID del archivo de Google Drive
# https://drive.google.com/file/d/1vzZ24iSQ7LZM9Rc3oSuIQmqzKp5-YFNO/view?usp=sharing
file_id = "1vzZ24iSQ7LZM9Rc3oSuIQmqzKp5-YFNO"
url = f"https://drive.google.com/uc?id={file_id}"

# Cargar el CSV en un DataFrame
dfRemoto = pd.read_csv(url)

# Mostrar los primeros registros
print(dfRemoto.shape)

# Convertir numéricas a enteros
for col in ['codigo_departamento', 'codigo_municipio', 'poblacion']:
    dfLocal[col] = pd.to_numeric(dfLocal[col], errors='coerce').fillna(0).astype(int)

# Validar texto (solo letras y espacios) en `departamento` y `municipio`
for col in ['departamento', 'municipio']:
    dfLocal = dfLocal[dfLocal[col].str.match(r'^[a-zA-Z\s]+$', na=False)]

# Resultado limpio
print("dfLocal después de la limpieza:")
print(dfLocal.shape)

# Transformar las columnas de fechas a filas
dfLocal = dfLocal.melt(
    id_vars=['departamento', 'codigo_departamento', 'municipio', 'codigo_municipio', 'poblacion'],
    var_name='fecha',
    value_name='casos_confirmados'
)

# Convertir la columna 'fecha' a formato de fecha
dfLocal['fecha'] = pd.to_datetime(dfLocal['fecha'], format='%m/%d/%Y', errors='coerce')

# Eliminar filas con fechas inválidas o casos confirmados no numéricos
dfLocal = dfLocal.dropna(subset=['fecha'])
dfLocal['casos_confirmados'] = pd.to_numeric(dfLocal['casos_confirmados'], errors='coerce').fillna(0).astype(int)

print(dfLocal.shape)

# Filtrar solo por Guatemala usando la columna 'Country' y 'Country_code'
dfRemoto = dfRemoto[
    (dfRemoto['Country'].str.lower() == 'guatemala') | (dfRemoto['Country_code'] == 'GT')
]
print(dfRemoto.shape)

# VALIDACIONES DE TIPOS DEL ARCHIVO REMOTO
for col in dfRemoto.columns:
  try:
    if col == "Date_reported":
      dfRemoto[col] = pd.to_datetime(dfRemoto[col], format='%m/%d/%Y', errors='coerce')
      dfRemoto.dropna(subset=[col], inplace=True)
  except Exception as e:
    print(e)

print(dfRemoto.shape)

print(dfRemoto.head())

# FILTRAR POR FECHAS DEL AÑO 2020
dfRemoto = dfRemoto[dfRemoto['Date_reported'].apply(lambda x: pd.to_datetime(x).year) == 2020]
print(dfRemoto.shape)

# ELIMINAR DUPLICADOS
dfRemoto = dfRemoto.drop_duplicates()
print(dfRemoto.shape)
print('Eliminación de duplicados realizada')

# Realizar la combinación por fechas
dfCombinado = pd.merge(
    dfLocal,
    dfRemoto,
    how='inner',  # Cambiar a 'left' si deseas mantener todas las filas de dfLocal
    left_on='fecha',
    right_on='Date_reported'
)

# Verificar el DataFrame combinado
print("Dataset combinado por fechas:")
print(dfCombinado.head())
print(dfRemoto.head())


# Verificar el tamaño del nuevo DataFrame
print("Tamaño del dataset combinado:", dfCombinado.shape)

# Eliminar columnas que no se necesitan para la tabla 'Departamento'
dfDepartamento = dfCombinado[['codigo_departamento', 'departamento']].drop_duplicates()

# Eliminar columnas que no se necesitan para la tabla 'Municipio'
dfMunicipio = dfCombinado[['codigo_municipio', 'municipio', 'codigo_departamento', 'poblacion']].drop_duplicates()

# Eliminar columnas que no se necesitan para la tabla 'DatosCovid'
dfDatosCovid = dfCombinado[['codigo_municipio', 'fecha', 'casos_confirmados', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']]

# Renombrar las columnas de dfDatosCovid para coincidir con las de la tabla SQL
dfDatosCovid.rename(columns={
    'New_cases': 'casos_nuevos',
    'New_deaths': 'muertes',
    'Cumulative_cases': 'casos_acumulativos',
    'Cumulative_deaths': 'muertes_acumulativas'
}, inplace=True)

# Eliminar columnas que no se necesitan para 'DatosCovid'
dfDatosCovid = dfDatosCovid[['codigo_municipio', 'fecha', 'casos_confirmados', 'casos_nuevos', 'muertes', 'casos_acumulativos', 'muertes_acumulativas']]

# Mostrar los primeros registros para cada DataFrame
print("Departamento:")
print(dfDepartamento.head())

print("Municipio:")
print(dfMunicipio.head())

print("DatosCovid:")
print(dfDatosCovid.head())

# Conexión a la base de datos
conexion = con.conectar_bd("practica1.db")

# Insertar datos en la tabla Departamento
con.insertar_departamento(conexion, dfDepartamento)

# Insertar datos en la tabla Municipio
con.insertar_municipio(conexion, dfMunicipio)

# Insertar datos en la tabla DatosCovid
con.insertar_datos_covid(conexion, dfDatosCovid)