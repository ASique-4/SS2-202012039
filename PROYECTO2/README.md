# PROYECTO 2

| Nombre                       | Carnet    |
| ---------------------------- | --------- |
| Angel Francisco Sique Santos | 202012039 |

---

# Página 1

![Página 1](./img/PROYECTO2%20(1)_page-0001.jpg)

**1. Gráfico de Barras Vertical (Suma de muertes por municipio):**

- **Motivo de la elección:** Los gráficos de barras son ideales para comparar cantidades entre diferentes categorías, en este caso, municipios. Permiten una fácil visualización de las diferencias en el número total de muertes entre cada uno.
- **Interpretación:** Las barras más altas representan los municipios con mayor número de muertes. Este gráfico permite identificar rápidamente los municipios con mayor y menor incidencia, así como observar la distribución general de las muertes entre los municipios. Se puede ver que hay unos pocos municipios con un número significativamente mayor de muertes que el resto.

**2. Mapa Geográfico (Suma de muertes por Ubicación Mapa):**

- **Motivo de la elección:** Los mapas son esenciales cuando la ubicación geográfica es un factor importante. En este caso, permite visualizar la distribución espacial de las muertes en el territorio de Guatemala.
- **Interpretación:** Los puntos o áreas coloreadas en el mapa representan la concentración de muertes en diferentes regiones. Permite identificar patrones geográficos, como posibles clusters (agrupaciones) de municipios con alta mortalidad, o regiones con menor incidencia. Al combinarlo con el gráfico de barras, se puede observar si los municipios con mayor número de muertes se concentran en una zona geográfica específica.

**3. Tabla con datos adicionales (TasaMortalidad100k, MaxFallecimientosDia, DiasRegistrados):**

- **Motivo de la elección:** Las tablas son útiles para presentar datos precisos y detallados. En este caso, complementan la información visual de los gráficos con valores numéricos específicos.
- **Interpretación:**
    - **TasaMortalidad100k (Tasa de Mortalidad por 100,000 habitantes):** Permite comparar la mortalidad entre municipios independientemente de su población. Un municipio con muchas muertes pero también mucha población puede tener una tasa similar a uno con menos muertes pero menos población.
    - **MaxFallecimientosDia (Máximo de Fallecimientos por Día):** Indica el pico máximo de muertes registrado en un solo día en cada municipio, lo que puede ser útil para identificar brotes o eventos específicos.
    - **DiasRegistrados (Días Registrados):** Indica el período de tiempo para el que se recopilaron los datos, lo que es crucial para contextualizar las cifras.

**4. Filtros interactivos (municipio):**

- **Motivo de la elección:** Los filtros permiten la exploración interactiva de los datos. Al seleccionar un municipio específico, se actualizan los demás gráficos y la tabla para mostrar la información correspondiente a ese municipio.
- **Interpretación:** Facilitan el análisis detallado de cada municipio individualmente. Al seleccionar un municipio, se puede ver su posición en el gráfico de barras, su ubicación en el mapa y sus valores específicos en la tabla.

**En resumen:** El panel utiliza una combinación efectiva de gráficos y una tabla para ofrecer una visión completa de los datos de mortalidad por municipio. El gráfico de barras y el mapa proporcionan una visión general de la distribución, mientras que la tabla y los filtros permiten un análisis más detallado de cada municipio. La interacción entre los elementos permite una exploración dinámica y un mejor entendimiento de la información.

# Página 2

![Página 2](./img/PROYECTO2%20(1)_page-0002.jpg)

**1. Gráfico de Líneas (Suma de muertes_acumulativas por Año, Mes y Día):**

- **Motivo de la elección:** Los gráficos de líneas son ideales para mostrar tendencias a lo largo del tiempo. En este caso, representan la acumulación de muertes desde una fecha inicial hasta una fecha final.
- **Interpretación:** La línea ascendente muestra el incremento en el número total de muertes a medida que avanza el tiempo. La pendiente de la línea indica la velocidad a la que se acumulan las muertes. Una pendiente más pronunciada indica un aumento más rápido, mientras que una pendiente menos pronunciada indica un aumento más lento. Se observa un aumento constante y pronunciado a partir de mediados de 2020.
- **Eje X (fecha):** Muestra el tiempo, con marcas que indican meses y años.
- **Eje Y (Suma de muertes acumulativas):** Muestra el número total de muertes acumuladas.

**2. Gráfico de Dispersión (Suma de muertes por poblacion):**

- **Motivo de la elección:** Los gráficos de dispersión se utilizan para mostrar la relación entre dos variables. En este caso, la relación entre la población y la suma de muertes.
- **Interpretación:** Cada punto en el gráfico representa una entidad (probablemente una región o un grupo). La posición del punto indica sus valores para ambas variables: la población en el eje horizontal (eje X) y la suma de muertes en el eje vertical (eje Y).
    - **Tendencia general:** Si los puntos muestran una tendencia ascendente de izquierda a derecha, esto sugiere una correlación positiva: a mayor población, mayor número de muertes.
    - **Puntos atípicos:** Los puntos que se alejan significativamente de la tendencia general se denominan valores atípicos (outliers). Estos puntos pueden representar regiones con tasas de mortalidad inusualmente altas o bajas en relación con su población. En el gráfico se ven algunos puntos que se desvían de una posible tendencia lineal.
- **Eje X (poblacion):** Representa el tamaño de la población.
- **Eje Y (Suma de muertes):** Representa el número total de muertes.

**3. Valor numérico (Suma de muertes_acumulativas: 124,49 mill.):**

- **Motivo de la elección:** Proporciona un valor numérico específico para la suma total de muertes acumuladas al final del período representado en el gráfico de líneas.
- **Interpretación:** Este número representa el total de muertes acumuladas durante el período de tiempo que se muestra en el gráfico de líneas. Es importante notar la escala, que en este caso es en millones (mill.).

**4. Control deslizante (debajo del gráfico de líneas):**

- **Motivo de la elección:** Permite al usuario seleccionar un rango de fechas específico para visualizar los datos.
- **Interpretación:** Al mover los extremos del control deslizante, se actualiza el gráfico de líneas para mostrar solo los datos correspondientes al período de tiempo seleccionado. Esto permite un análisis más detallado de períodos específicos.

**En resumen:** Este panel muestra la evolución de las muertes acumuladas a lo largo del tiempo y su relación con la población. El gráfico de líneas muestra la tendencia temporal, mientras que el gráfico de dispersión explora la correlación entre la población y la cantidad de muertes. El valor numérico proporciona un resumen del total de muertes acumuladas, y el control deslizante permite la exploración interactiva de diferentes períodos de tiempo.

# Página 3

![Página 3](./img/PROYECTO2%20(1)_page-0003.jpg)

**1. Valor numérico (TasaMortalidad100k):**

- **Motivo de la elección:** Proporciona un valor numérico conciso para la tasa de mortalidad general.
- **Interpretación:** Indica que la tasa de mortalidad general es de 6,15 por cada 100,000 habitantes. Este valor sirve como referencia para comparar con las tasas específicas de cada departamento.

**2. Nombre del Departamento:**

- **Motivo de la elección:** Indica el departamento que tiene la primera fecha registrada en los datos.
- **Interpretación:** Señala que los datos de ALTA VERAPAZ fueron los primeros en ser registrados. Esto podría ser relevante para entender el contexto temporal de los datos.

**3. Gráfico de Líneas (TasaMortalidad100kDepartamento por departamento):**

- **Motivo de la elección:** Los gráficos de líneas son útiles para mostrar tendencias y comparaciones entre diferentes categorías, en este caso, departamentos.
- **Interpretación:** La línea descendente muestra la variación en la tasa de mortalidad entre los diferentes departamentos. Permite identificar rápidamente los departamentos con las tasas más altas y más bajas.
- **Eje X (departamento):** Muestra los nombres de los departamentos. Están ordenados de mayor a menor tasa de mortalidad.
- **Eje Y (TasaMortalidad100kDepartamento):** Muestra la tasa de mortalidad por 100,000 habitantes para cada departamento.

**4. Gráfico de Pastel (MuertesTotalesDepartamento por departamento):**

- **Motivo de la elección:** Los gráficos de pastel son útiles para mostrar la proporción de cada parte en relación con el todo. En este caso, la proporción de muertes totales en cada departamento con respecto al total de muertes.
- **Interpretación:** Cada porción del pastel representa un departamento, y el tamaño de la porción es proporcional al número total de muertes en ese departamento. Permite visualizar rápidamente qué departamentos contribuyen más al total de muertes. Se observan algunas porciones más grandes que indican una mayor concentración de muertes en esos departamentos.
- **Leyenda:** La leyenda a la derecha del gráfico asocia cada color con un departamento.

**Relación entre los gráficos:**

El gráfico de líneas se centra en la _tasa_ de mortalidad, mientras que el gráfico de pastel se centra en el número _total_ de muertes. Es importante notar que un departamento con una alta tasa de mortalidad no necesariamente tendrá el mayor número total de muertes, y viceversa. Por ejemplo, un departamento con una población pequeña podría tener una alta tasa de mortalidad pero un número total de muertes menor que un departamento con una población grande y una tasa de mortalidad más baja.

**En resumen:** El panel proporciona una visión completa de la mortalidad por departamento, mostrando tanto la tasa como el número total de muertes. El gráfico de líneas facilita la comparación de las tasas entre departamentos, mientras que el gráfico de pastel muestra la distribución de las muertes totales. La información combinada permite un análisis más profundo y matizado de la situación.

# Página 4

![Página 4](./img/PROYECTO2%20(1)_page-0004.jpg)

**1. Gráfico de Barras (Suma de muertes por departamento):**

- **Motivo de la elección:** Los gráficos de barras son ideales para comparar cantidades entre diferentes categorías, en este caso, los departamentos. Permiten una fácil visualización de las diferencias en el número total de muertes entre cada uno.
- **Interpretación:** Las barras más altas representan los departamentos con mayor número de muertes. Se observa claramente que algunos departamentos, como HUEHUETENANGO, SAN MARCOS y QUETZALTENANGO, tienen un número significativamente mayor de muertes que el resto.
- **Eje X (departamento):** Muestra los nombres de los departamentos.
- **Eje Y (Suma de muertes):** Muestra el número total de muertes.

**2. Gráfico de Pastel (Suma de poblacion por departamento):**

- **Motivo de la elección:** Los gráficos de pastel son útiles para mostrar la proporción de cada parte en relación con el todo. En este caso, la proporción de la población de cada departamento con respecto a la población total.
- **Interpretación:** Cada porción del pastel representa un departamento, y el tamaño de la porción es proporcional a la población de ese departamento. Permite visualizar rápidamente qué departamentos tienen una mayor proporción de la población total. Se observan algunas porciones más grandes que indican una mayor concentración de población en esos departamentos.
- **Leyenda:** La leyenda a la derecha del gráfico asocia cada color con un departamento. Se muestran también los valores numéricos y el porcentaje que representa cada departamento de la población total.

**3. Valor numérico (PorcentajeMuertesPoblacion: 6,15):**

- **Motivo de la elección:** Proporciona un valor numérico que relaciona las muertes con la población. Sin embargo, tal como está nombrado, "PorcentajeMuertesPoblacion", es ambiguo. Lo más probable es que se refiera a la Tasa de Mortalidad por 100,000 habitantes, como en paneles anteriores.
- **Interpretación:** Asumiendo que se refiere a la Tasa de Mortalidad por 100,000 habitantes, indica que, en promedio, hay 6,15 muertes por cada 100,000 habitantes. Es importante notar que este es un valor promedio a nivel general y no representa la tasa específica de cada departamento.

**4. Valor numérico (PromedioMuertesDiariasDepartamento: 6,53 mil):**

- **Motivo de la elección:** Proporciona un valor numérico para el promedio de muertes diarias por departamento.
- **Interpretación:** Indica que, en promedio, hay 6,53 mil muertes diarias por departamento. Al igual que con la Tasa de Mortalidad general, este es un valor promedio y no representa el promedio diario específico de cada departamento.

**Relación entre los gráficos:**

La combinación de ambos gráficos permite comparar la distribución de las muertes con la distribución de la población. Es crucial entender que un departamento con una gran cantidad de muertes no necesariamente tiene una alta tasa de mortalidad si también tiene una gran población. De igual manera, un departamento con pocas muertes podría tener una alta tasa de mortalidad si su población es muy pequeña.

**En resumen:** El panel proporciona una visión general de la distribución de muertes y población por departamento. El gráfico de barras muestra la cantidad total de muertes, el gráfico de pastel muestra la proporción de la población, y los valores numéricos proporcionan información sobre la tasa de mortalidad promedio y el promedio de muertes diarias.

# Página 5

![Página 5](./img/PROYECTO2%20(1)_page-0005.jpg)

**1. Gráfico de Líneas Múltiples (Suma de muertes por Año, Mes, Día y departamento):**

- **Motivo de la elección:** Los gráficos de líneas son ideales para mostrar tendencias a lo largo del tiempo, y al usar múltiples líneas, se pueden comparar las tendencias de diferentes categorías, en este caso, los departamentos.
- **Interpretación:** Cada línea representa un departamento diferente. La altura de la línea en un punto dado en el tiempo indica el número de muertes en ese departamento en ese momento. Se pueden observar varios aspectos:
    - **Tendencia general:** Se observa un aumento general en las muertes a partir de mediados de 2020, con picos pronunciados en ciertos momentos.
    - **Comparación entre departamentos:** Se pueden comparar las tendencias entre los diferentes departamentos. Algunas líneas muestran picos más altos o un aumento más rápido que otras, lo que indica diferencias en la incidencia de muertes entre los departamentos a lo largo del tiempo. Se observa que algunas líneas (principalmente la naranja) sobresalen del resto, indicando un departamento con un número de muertes significativamente mayor en ciertos periodos.
    - **Picos:** Los picos en las líneas representan momentos de aumento significativo en las muertes. Comparar la ubicación temporal de estos picos entre los departamentos puede revelar patrones o eventos que afectaron a múltiples regiones simultáneamente.
- **Eje X (Año):** Muestra el tiempo, con marcas que indican meses y años.
- **Eje Y (Suma de muertes):** Muestra el número total de muertes.
- **Leyenda (a la derecha):** Asocia cada color con un departamento.

**2. Información adicional:**

- **Primera fecha: departamento ALTA VERAPAZ:** Indica que los primeros datos registrados corresponden a este departamento.
- **Suma de muertes: 1 mill.:** Este valor parece ser redundante y poco claro en este contexto. Dado que el gráfico ya muestra la suma de muertes para cada departamento a lo largo del tiempo, mostrar un valor único de "1 mill." no aporta información útil. Probablemente se refiere a la escala del eje Y (que llega hasta 4 mil).

**En resumen:** Este panel se centra en la evolución temporal de las muertes en cada departamento. El gráfico de líneas múltiples permite comparar las tendencias entre los departamentos e identificar picos o patrones comunes.

