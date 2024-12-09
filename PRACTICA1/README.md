# PROYECTO 2

| Nombre                       | Carnet    |
| ---------------------------- | --------- |
| Angel Francisco Sique Santos | 202012039 |

---

# Índice

1. [Introducción](#introducción)
2. [Proceso de ETL](#proceso-de-etl)
   - [1. Extracción de Datos](#1-extracción-de-datos)
     - [1.1 Cargar datos locales (`municipio.csv`)](#11-cargar-datos-locales-municipiocsv)
     - [1.2 Descargar y cargar datos globales desde Google Drive](#12-descargar-y-cargar-datos-globales-desde-google-drive)
   - [2. Transformación de Datos](#2-transformación-de-datos)
     - [2.1 Limpieza del archivo local (`municipio.csv`)](#21-limpieza-del-archivo-local-municipiocsv)
       - [Conversión de columnas numéricas](#conversión-de-columnas-numéricas)
       - [Validación de columnas de texto](#validación-de-columnas-de-texto)
       - [Transformar fechas dinámicas en filas](#transformar-fechas-dinámicas-en-filas)
       - [Formateo y validación de fechas](#formateo-y-validación-de-fechas)
     - [2.2 Limpieza del archivo remoto (`global_calificacion.csv`)](#22-limpieza-del-archivo-remoto-global_calificacioncsv)
       - [Filtrar datos de Guatemala](#filtrar-datos-de-guatemala)
       - [Formateo de fechas y eliminación de valores no válidos](#formateo-de-fechas-y-eliminación-de-valores-no-válidos)
       - [Filtrar por el año 2020](#filtrar-por-el-año-2020)
       - [Eliminar duplicados](#eliminar-duplicados)
     - [2.3 Combinación de datos](#23-combinación-de-datos)
   - [3. Preparación de Tablas para SQL](#3-preparación-de-tablas-para-sql)
     - [Tabla `Departamento`](#tabla-departamento)
     - [Tabla `Municipio`](#tabla-municipio)
     - [Tabla `DatosCovid`](#tabla-datoscovid)
   - [4. Carga a la Base de Datos](#4-carga-a-la-base-de-datos)

---

### **Introducción**

Este proyecto implementa un proceso de ETL (*Extract, Transform, Load*) para procesar datos relacionados con casos de COVID-19. Los datos combinan información local de municipios y datos globales de la pandemia.

---

### **Proceso de ETL**

## **1. Extracción de Datos**

### **1.1 Cargar datos locales (`municipio.csv`)**
```python
dfLocal = pd.read_csv('municipio.csv')
```
- **Descripción**: Carga un archivo CSV que contiene información de los municipios de Guatemala. Este archivo tiene columnas como:
  - `departamento`: Nombre del departamento.
  - `codigo_departamento`: Código único del departamento.
  - `municipio`: Nombre del municipio.
  - `codigo_municipio`: Código único del municipio.
  - `poblacion`: Población del municipio.
  - Fechas: Datos de casos confirmados registrados por fechas específicas.

---

### **1.2 Descargar y cargar datos globales desde Google Drive**
```python
file_id = "1vzZ24iSQ7LZM9Rc3oSuIQmqzKp5-YFNO"
url = f"https://drive.google.com/uc?id={file_id}"
dfRemoto = pd.read_csv(url)
```
- **Descripción**: Se descarga programáticamente un archivo CSV desde Google Drive utilizando su ID. El archivo contiene datos globales de casos y muertes por COVID-19.
- **Campos importantes**:
  - `Date_reported`: Fecha de reporte.
  - `Country`: País.
  - `Country_code`: Código ISO del país.
  - `New_cases`: Nuevos casos confirmados en la fecha.
  - `New_deaths`: Nuevas muertes confirmadas en la fecha.

---

## **2. Transformación de Datos**

### **2.1 Limpieza del archivo local (`municipio.csv`)**

#### **Conversión de columnas numéricas**
```python
for col in ['codigo_departamento', 'codigo_municipio', 'poblacion']:
    dfLocal[col] = pd.to_numeric(dfLocal[col], errors='coerce').fillna(0).astype(int)
```
- **Objetivo**: Convertir columnas clave a enteros, manejando errores y valores nulos.
- **Explicación**:
  - `pd.to_numeric`: Convierte los datos a formato numérico.
  - `errors='coerce'`: Los valores no válidos se convierten en `NaN`.
  - `fillna(0)`: Sustituye los valores nulos por 0.
  - `astype(int)`: Convierte los valores finales a enteros.

#### **Validación de columnas de texto**
```python
for col in ['departamento', 'municipio']:
    dfLocal = dfLocal[dfLocal[col].str.match(r'^[a-zA-Z\s]+$', na=False)]
```
- **Objetivo**: Validar que las columnas de texto contengan únicamente letras y espacios.
- **Explicación**:
  - `str.match`: Aplica una expresión regular para verificar el formato del texto.
  - `^[a-zA-Z\s]+$`: Permite únicamente letras y espacios.

#### **Transformar fechas dinámicas en filas**
```python
dfLocal = dfLocal.melt(
    id_vars=['departamento', 'codigo_departamento', 'municipio', 'codigo_municipio', 'poblacion'],
    var_name='fecha',
    value_name='casos_confirmados'
)
```
- **Objetivo**: Convertir columnas de fechas en filas para estructurar mejor los datos.
- **Explicación**:
  - `id_vars`: Mantiene las columnas fijas (que no se transforman).
  - `var_name`: Define el nombre de la columna que contendrá las fechas.
  - `value_name`: Define el nombre de la columna con los valores de casos confirmados.

#### **Formateo y validación de fechas**
```python
dfLocal['fecha'] = pd.to_datetime(dfLocal['fecha'], format='%m/%d/%Y', errors='coerce')
dfLocal = dfLocal.dropna(subset=['fecha'])
```
- **Objetivo**: Convertir la columna `fecha` al formato `datetime` y eliminar valores no válidos.
- **Explicación**:
  - `pd.to_datetime`: Convierte las fechas al formato estándar `datetime`.
  - `errors='coerce'`: Los valores no válidos se convierten en `NaT` (Not a Time).
  - `dropna`: Elimina filas donde la fecha es inválida.

---

### **2.2 Limpieza del archivo remoto (`global_calificacion.csv`)**

#### **Filtrar datos de Guatemala**
```python
dfRemoto = dfRemoto[
    (dfRemoto['Country'].str.lower() == 'guatemala') | (dfRemoto['Country_code'] == 'GT')
]
```
- **Objetivo**: Seleccionar únicamente los datos correspondientes a Guatemala.
- **Explicación**:
  - Filtra las filas donde `Country` sea "Guatemala" o `Country_code` sea "GT".

#### **Formateo de fechas y eliminación de valores no válidos**
```python
dfRemoto['Date_reported'] = pd.to_datetime(dfRemoto['Date_reported'], format='%m/%d/%Y', errors='coerce')
dfRemoto.dropna(subset=['Date_reported'], inplace=True)
```
- **Objetivo**: Convertir `Date_reported` a formato `datetime` y eliminar valores nulos.

#### **Filtrar por el año 2020**
```python
dfRemoto = dfRemoto[dfRemoto['Date_reported'].dt.year == 2020]
```
- **Objetivo**: Seleccionar únicamente los datos del año 2020.

#### **Eliminar duplicados**
```python
dfRemoto = dfRemoto.drop_duplicates()
```
- **Objetivo**: Eliminar filas duplicadas.

---

### **2.3 Combinación de datos**
```python
dfCombinado = pd.merge(
    dfLocal,
    dfRemoto,
    how='inner',
    left_on='fecha',
    right_on='Date_reported'
)
```
- **Objetivo**: Combinar ambos datasets por la columna de fechas.
- **Explicación**:
  - `left_on`: Columna de fechas en `dfLocal`.
  - `right_on`: Columna de fechas en `dfRemoto`.
  - `how='inner'`: Combina únicamente las filas que coinciden en ambos DataFrames.

---

### **3. Preparación de Tablas para SQL**

#### **Tabla `Departamento`**
```python
dfDepartamento = dfCombinado[['codigo_departamento', 'departamento']].drop_duplicates()
```

#### **Tabla `Municipio`**
```python
dfMunicipio = dfCombinado[['codigo_municipio', 'municipio', 'codigo_departamento', 'poblacion']].drop_duplicates()
```

#### **Tabla `DatosCovid`**
```python
dfDatosCovid = dfCombinado[['codigo_municipio', 'fecha', 'casos_confirmados', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']]
dfDatosCovid.rename(columns={
    'New_cases': 'casos_nuevos',
    'New_deaths': 'muertes',
    'Cumulative_cases': 'casos_acumulativos',
    'Cumulative_deaths': 'muertes_acumulativas'
}, inplace=True)
```

---

### **4. Carga a la Base de Datos**
```python
conexion = con.conectar_bd("practica1.db")
con.insertar_departamento(conexion, dfDepartamento)
con.insertar_municipio(conexion, dfMunicipio)
con.insertar_datos_covid(conexion, dfDatosCovid)
```
- **Objetivo**: Insertar los datos procesados en las tablas SQL:
  - **`Departamento`**: Contiene los datos de departamentos.
  - **`Municipio`**: Contiene los datos de municipios.
  - **`DatosCovid`**: Contiene los datos de COVID-19.

---

Con esta documentación detallada, cada paso del código queda claramente explicado, desde la extracción de datos hasta la carga en SQL. ¿Hay algún punto que necesites ajustar o expandir? 😊