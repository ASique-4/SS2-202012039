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
      - [Explicación del archivo `coneccionsql.py`](#explicación-del-archivo-coneccionsqlpy)
        - [1. Conexión a la base de datos](#1-conexión-a-la-base-de-datos)
        - [2. Inserción de Datos en Bloques](#2-inserción-de-datos-en-bloques)
        - [3. Funciones para Insertar Datos Específicos en las Tablas](#3-funciones-para-insertar-datos-específicos-en-las-tablas)
          - [Insertar en la tabla `Departamento`](#insertar-en-la-tabla-departamento)
          - [Insertar en la tabla `Municipio`](#insertar-en-la-tabla-municipio)
          - [Insertar en la tabla `DatosCovid`](#insertar-en-la-tabla-datoscovid)
      - [Explicación de la Estructura de las Tablas SQL](#explicación-de-la-estructura-de-las-tablas-sql)
        - [1. Tabla `Departamento`](#1-tabla-departamento)
        - [2. Tabla `Municipio`](#2-tabla-municipio)
        - [3. Tabla `DatosCovid`](#3-tabla-datoscovid)
      - [Relaciones entre las Tablas](#relaciones-entre-las-tablas)
      - [¿Por qué esta estructura?](#¿por-qué-esta-estructura)
      - [Notas Importantes](#notas-importantes)
    - [¿Por qué eliminamos algunas columnas y por qué no son relevantes para mostrar?](#¿por-qué-eliminamos-algunas-columnas-y-por-qué-no-son-relevantes-para-mostrar)
    - [¿Por qué limpiamos los datos como lo hicimos?](#¿por-qué-limpiamos-los-datos-como-lo-hicimos)

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

### **Explicación del archivo `coneccionsql.py`**

Este archivo contiene funciones para conectarse a una base de datos SQLite y para insertar datos en tres tablas (`Departamento`, `Municipio` y `DatosCovid`). A continuación se explican en detalle las funcionalidades de cada sección del archivo.

---

### **1. Conexión a la Base de Datos**

```python
def conectar_bd(nombre_bd):
    try:
        conexion = sqlite3.connect(nombre_bd)
        print("Conexión exitosa a la base de datos")
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
```

- **Propósito**: Esta función establece una conexión con la base de datos SQLite.
- **Parámetro**:
  - `nombre_bd`: Nombre del archivo de la base de datos, que puede ser algo como `"practica1.db"`.
- **Flujo**:
  1. Intenta conectarse a la base de datos usando `sqlite3.connect()`.
  2. Si la conexión es exitosa, devuelve el objeto de conexión.
  3. Si ocurre un error (por ejemplo, si la base de datos no existe o no se puede acceder), captura la excepción y muestra un mensaje de error.
- **Ejemplo de uso**:
  ```python
  conexion = conectar_bd("practica1.db")
  ```

---

### **2. Inserción de Datos en Bloques**

```python
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
```

- **Propósito**: Insertar datos en la base de datos en bloques de 50 registros para optimizar el proceso de carga y evitar problemas de memoria o sobrecarga.
- **Parámetros**:
  - `conexion`: Objeto de conexión SQLite obtenido de la función `conectar_bd`.
  - `df`: DataFrame que contiene los datos a insertar.
  - `tabla`: Nombre de la tabla a la que se insertarán los datos (puede ser `Departamento`, `Municipio`, o `DatosCovid`).
- **Flujo**:
  1. Divide los datos del DataFrame en bloques de 50 registros.
  2. Para cada bloque, intenta insertarlo en la tabla usando `to_sql()`.
  3. Si un bloque no se inserta correctamente, se registra como fallido y se guarda el rango de filas.
  4. Después de intentar todos los bloques, se reintentan aquellos que fallaron.
  5. Finalmente, se imprime un reporte de cuántos bloques fueron insertados con éxito y cuántos fallaron.

- **Ejemplo de uso**:
  ```python
  insertar_en_bloques(conexion, dfMunicipio, 'Municipio')
  ```

---

### **3. Funciones para Insertar Datos Específicos en las Tablas**

#### **Insertar en la tabla `Departamento`**
```python
def insertar_departamento(conexion, df_departamento):
    insertar_en_bloques(conexion, df_departamento, 'Departamento')
```

- **Propósito**: Llama a la función `insertar_en_bloques` para insertar los datos en la tabla `Departamento`.
- **Parámetros**:
  - `conexion`: Objeto de conexión SQLite.
  - `df_departamento`: DataFrame con los datos a insertar en la tabla `Departamento`.

---

#### **Insertar en la tabla `Municipio`**
```python
def insertar_municipio(conexion, df_municipio):
    insertar_en_bloques(conexion, df_municipio, 'Municipio')
```

- **Propósito**: Llama a la función `insertar_en_bloques` para insertar los datos en la tabla `Municipio`.
- **Parámetros**:
  - `conexion`: Objeto de conexión SQLite.
  - `df_municipio`: DataFrame con los datos a insertar en la tabla `Municipio`.

---

#### **Insertar en la tabla `DatosCovid`**
```python
def insertar_datos_covid(conexion, df_datos_covid):
    insertar_en_bloques(conexion, df_datos_covid, 'DatosCovid')
```

- **Propósito**: Llama a la función `insertar_en_bloques` para insertar los datos en la tabla `DatosCovid`.
- **Parámetros**:
  - `conexion`: Objeto de conexión SQLite.
  - `df_datos_covid`: DataFrame con los datos a insertar en la tabla `DatosCovid`.

---

### **Explicación de la Estructura de las Tablas SQL**

La estructura de las tablas en la base de datos está diseñada de acuerdo con las necesidades del proyecto, en el cual se manejan datos sobre los municipios de Guatemala y los casos de COVID-19. El modelo sigue principios de **normalización** y **relaciones entre tablas** para asegurar la integridad de los datos y optimizar el rendimiento.

---

### **1. Tabla `Departamento`**

```sql
CREATE TABLE Departamento (
  codigo_departamento INT PRIMARY KEY,
  departamento VARCHAR(100) NOT NULL
);
```

- **Propósito**: Almacenar información de los departamentos de Guatemala.
- **Columnas**:
  - **`codigo_departamento`**: Es la clave primaria de la tabla, lo que significa que cada departamento tendrá un identificador único. Este campo es esencial para poder hacer referencias entre tablas y garantizar que no haya duplicados en los departamentos.
  - **`departamento`**: Nombre del departamento. Es un campo **NOT NULL** para asegurar que siempre se almacene un nombre de departamento, evitando valores vacíos.

- **Razón de la estructura**:
  - Se utiliza una **clave primaria** (`codigo_departamento`) para identificar de manera única cada departamento.
  - Este diseño permite que otros datos, como los municipios, se relacionen fácilmente con un departamento a través de la clave foránea (`codigo_departamento`).

---

### **2. Tabla `Municipio`**

```sql
CREATE TABLE Municipio (
  codigo_municipio INT PRIMARY KEY,
  municipio VARCHAR(100) NOT NULL,
  codigo_departamento INT,
  poblacion INT,
  FOREIGN KEY (codigo_departamento) REFERENCES Departamento(codigo_departamento)
);
```

- **Propósito**: Almacenar información de los municipios y su relación con los departamentos.
- **Columnas**:
  - **`codigo_municipio`**: Clave primaria de la tabla `Municipio`. Identifica de manera única cada municipio.
  - **`municipio`**: Nombre del municipio. Es un campo **NOT NULL**, lo que asegura que cada municipio tenga un nombre.
  - **`codigo_departamento`**: Clave foránea que hace referencia al `codigo_departamento` de la tabla `Departamento`. Establece una relación entre los municipios y los departamentos a los que pertenecen.
  - **`poblacion`**: Número de habitantes del municipio. Este campo no tiene restricciones, pero es importante para representar la población de cada municipio.

- **Razón de la estructura**:
  - Se establece una **relación de clave foránea** entre `Municipio` y `Departamento` utilizando `codigo_departamento`. Esto asegura que cada municipio esté vinculado a un departamento existente en la tabla `Departamento`.
  - La **clave primaria** (`codigo_municipio`) garantiza que cada municipio sea único.
  - Esta estructura permite consultas eficientes sobre los municipios y sus respectivas poblaciones, y facilita la asociación entre municipios y sus departamentos.

---

### **3. Tabla `DatosCovid`**

```sql
CREATE TABLE DatosCovid (
  id INT PRIMARY KEY,
  codigo_municipio INT,
  fecha DATE NOT NULL,
  casos_confirmados INT,
  casos_recuperados INT,
  muertes INT,
  FOREIGN KEY (codigo_municipio) REFERENCES Municipio(codigo_municipio)
);
```

- **Propósito**: Almacenar los datos de casos de COVID-19 asociados a cada municipio y fecha.
- **Columnas**:
  - **`id`**: Clave primaria de la tabla `DatosCovid`. Esta columna se usa para identificar de manera única cada registro de datos de COVID-19.
  - **`codigo_municipio`**: Clave foránea que hace referencia a `codigo_municipio` en la tabla `Municipio`. Relaciona los datos de COVID-19 con el municipio correspondiente.
  - **`fecha`**: Fecha del reporte de casos de COVID-19. Es un campo **NOT NULL** para garantizar que siempre haya una fecha asociada a cada registro.
  - **`casos_confirmados`**: Número de casos confirmados en esa fecha para el municipio.
  - **`casos_recuperados`**: Número de casos recuperados en esa fecha.
  - **`muertes`**: Número de muertes reportadas en esa fecha.

- **Razón de la estructura**:
  - La **clave primaria** (`id`) garantiza que cada entrada en la tabla de datos sea única, independientemente del municipio o la fecha.
  - La **clave foránea** (`codigo_municipio`) establece la relación entre los datos de COVID-19 y los municipios específicos, permitiendo acceder a los datos por municipio.
  - Se almacenan los **casos confirmados**, **casos recuperados** y **muertes** como campos separados, lo que permite un análisis detallado de la situación de COVID-19 a nivel de municipio.
  - La **fecha** es clave para el análisis temporal, ya que cada entrada corresponde a un reporte específico de un día determinado.

---

### **Relaciones entre las Tablas**

1. **Relación entre `Departamento` y `Municipio`**:
   - Cada **`Municipio`** está asociado a un **`Departamento`** a través de la columna `codigo_departamento` en la tabla `Municipio`. Esto permite consultas que se basen en la jerarquía de los datos (e.g., obtener todos los municipios de un departamento específico).

2. **Relación entre `Municipio` y `DatosCovid`**:
   - Cada **`DatosCovid`** está asociado a un **`Municipio`** a través de la columna `codigo_municipio`. Esto vincula los datos de COVID-19 con los municipios y permite consultar los casos y muertes para cada municipio en una fecha específica.

---

### **¿Por qué esta estructura?**

Esta estructura de base de datos normalizada permite:
- **Eficiencia**: Los datos están organizados de manera que se minimiza la redundancia y se optimiza el rendimiento de las consultas.
- **Integridad**: Las claves primarias y foráneas aseguran que no haya registros duplicados y que las relaciones entre departamentos, municipios y datos de COVID sean coherentes.
- **Flexibilidad**: La base de datos es lo suficientemente flexible para permitir el análisis por municipio, departamento y fecha, lo que facilita la toma de decisiones basadas en los datos de COVID-19.


### **Notas Importantes**

1. **Uso de Bloques para Insertar Datos**:
   - Dividir los datos en bloques de 50 registros ayuda a evitar problemas de memoria o de sobrecarga al insertar grandes cantidades de datos a la base de datos.
   - También mejora el rendimiento de la base de datos, ya que las inserciones en bloques reducen el tiempo de ejecución en comparación con las inserciones de registros individuales.

2. **Manejo de Errores**:
   - Si ocurre un error durante la inserción de un bloque, se captura la excepción y se agrega el índice del bloque fallido a la lista `fallidos_indices`. Luego, el bloque fallido se reintenta en una segunda fase.
   - Esto garantiza que incluso si algunas inserciones fallan, los datos restantes se insertan correctamente.

3. **Optimización de Inserciones**:
   - Se usa `if_exists='append'` en `to_sql()` para agregar datos a la tabla sin eliminar los registros existentes. De esta manera, los datos nuevos se agregan a las tablas sin sobrescribir los datos previos.

---

### **¿Por qué eliminamos algunas columnas y por qué no son relevantes para mostrar?**

Al procesar los datos, eliminamos columnas que no eran necesarias para los objetivos del análisis ni para el esquema definido en la base de datos. Estas columnas, aunque relevantes en el contexto original de los datasets, no aportaban valor en el análisis final o en el modelo de datos. Por ejemplo:

- **En el archivo global**: Columnas como `WHO_region` y `Country_code` no eran necesarias porque:
  - `WHO_region` identifica la región global (e.g., AMRO), pero no agrega información útil para el análisis enfocado en Guatemala.
  - `Country_code` es redundante al trabajar únicamente con datos filtrados para `Country == Guatemala`.
- **En el archivo local**: Las columnas de fechas individuales fueron transformadas en una estructura de filas para normalizar los datos y facilitar la combinación con otros datasets. Esto permitió usar un formato estándar que facilita el análisis temporal.

Eliminamos estas columnas para reducir la complejidad del dataset, optimizar la carga en la base de datos y evitar almacenar datos irrelevantes que solo ocuparían espacio sin utilidad práctica.

---

### **¿Por qué limpiamos los datos como lo hicimos?**

El proceso de limpieza de datos es crucial para garantizar la calidad y consistencia de la información que se utilizará en análisis posteriores. Aquí está la razón detrás de las decisiones de limpieza aplicadas:

1. **Conversión de columnas numéricas**:
   - Algunas columnas contenían valores no numéricos o nulos debido a errores en los datos originales. Los convertimos a enteros utilizando `pd.to_numeric` con `errors='coerce'` para manejar estos errores y reemplazamos valores nulos con `0`. Esto asegura que todos los cálculos posteriores sean consistentes y que no se produzcan errores por tipos de datos.

2. **Validación de texto en columnas**:
   - Las columnas `departamento` y `municipio` se validaron para contener únicamente letras y espacios mediante una expresión regular. Esto garantiza que no existan valores inválidos o caracteres inesperados, como números o símbolos, que podrían indicar errores en la entrada de datos.

3. **Transformación de fechas a filas**:
   - En el archivo local, las columnas de fechas individuales se transformaron en filas para normalizar los datos. Este enfoque sigue el principio de una base de datos relacional, donde las fechas se representan como una columna única. Esto facilita la combinación con otros datasets (como el global) y permite realizar análisis temporales.

4. **Filtrado de datos globales por país y año**:
   - Filtramos los datos del archivo global para incluir únicamente registros de Guatemala y del año 2020. Esto eliminó datos irrelevantes de otros países y años, asegurando que el análisis estuviera enfocado en los objetivos del proyecto.

5. **Conversión y validación de fechas**:
   - Convertimos las fechas a un formato estándar (`datetime`) y eliminamos filas con fechas inválidas (`NaT`). Esto fue necesario para garantizar que las operaciones temporales (como filtros o combinaciones) se realizaran correctamente.

6. **Eliminación de duplicados**:
   - Al eliminar filas duplicadas en los datasets, garantizamos que no hubiera redundancia en los datos almacenados en la base de datos. Esto mejora la integridad de los datos y evita errores en análisis futuros.
