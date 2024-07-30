
HENRY </p>
Proyecto Individual 1 </p>
Sistema de Recomendación de Peliculas
=======
# Proyecto Individual 1
Henry DataPT9 
</p>
Maria Isabel Arango
</p>


## Introducción:

En este proyecto tomo el roll de **`Data Scientist`** en una start-up que provee servicios de agregación de plataformas de streaming. 
Los datos no cuentan con la madurez necesaria por lo que, para poder realizar el proyecto, se requiere un trabajpásoo previo de limpieza y análisis.
El objetivo de este proyecto es crear un modelo de recomendación de películas con la información suministrada.

A continuación se explica el paso a paso del desarrollo de este proyecto.

## Desarrollo:

**1. Limpieza de Datos:**
   En este paso se realiza el cargue y un análisis inicial de datos de los dataset movies_dataset.csv y credits.csv, con el fin de limpiarlos y prepararlos para su uso. (Ver archivo **´Data_Engineering.ipyn´** :eyes: ).
   </p>
   En el este notebook se carga la información de los 2 datasets: (data_movies.csv y data_credist.csv). </p>
   
   **En data_Movies:**
   
   </p>
   
   **a.** Se reviza de la información del datasets (Descripción, visualización de encabezados e información general y forma)</p>
   **b.** Elimina los duplicados presentes en el dataset.</p>
   **c.** Elimina columnas inicialmente detectadas que no serán utilizadas ('video','imdb_id','adult','original_title','poster_path','homepage')</p>
   **d.** Se desanidan las columnas: 'belongs_to_collection', 'production_companies', 'production_countries', 'spoken_languages' y 'genres'. </p>
   **e.** Realiza tratamiento a los valores NaN (vacíos). </p>
   **f.** Elimina las columnas resultantes de desanidar cuyos valores nulos sean superiores al 50% de los datos.</p>
   **g.** Calcula el retorno de la inversión en moneda y en porcentaje creandose las columnas 'return' y 'returno_US'. 
      Se usan las siguientes formulas </p> 
      retorno_US = retorno en moneda = (ingresos - presupuesto ) </p> 
      return = retorno en % = (ingresos - presupuesto) / presupuesto ) en la columna </p>
   **h.** Limpia la información del titulo de las peliculas 'title': aseguro que los datos sean cadenas de texto (str), convierto a minusculas, elimino espacios en blanco.</p>
   
   **En Data_Credits:**

   </p>
   
   **a.**
   Se reviza de la información del datasets (Descripción, visualización de encabezados e información general y forma)</p>
   **b.** Elimina los duplicados presentes en el dataset.</p>
   **c.** Se eliminan duplicados.
   **d.** Se desanidan las columnas: 'cast' y 'crew', obteniendo la información de los actores y los creditos de la pelicula.</p>
   **e.** Se elimina las columnas resultantes de desanidar 'crew' escepto 'director', y las de 'cast' cuyos valores nulos sean superiores al 50% de los datos.</p>
   </p>
   Finalmete se exportan los archivos a formato .parquet para usarlos posteriormente en la API. Obtengo: </p>

   :eyes: **`data_movies.parquet`** 
   :eyes: **`data_credits.parquet`** :eyes: 
   </p>

   
**2. Analisis de Datos EDA:** Se realiza un análisis gráfico y de las características de los datos de los datasets.(Ver archivo **´EDA.ipyn´** :eyes: ):   </p>

**a.** Cargar los archivos ya en formato parquet. data_movies.parquet y data_credits.parquet. </p>
**b.** Revisar los datos de encabezado, la información de número de columnas, nombres de titulos y cantidad de información. </p>
**c.** Ver un análisis estadistico de las variables numericas: cantidad, promedio, desviación standard, valores maximo y minimo; y percentil 25, 50 y 75. </p>
**d.** Analisis gráfico con histograma de las variables numericas: 'budget', 'popularity', 'revenue', 'runtime', 'vote_average', 'vote_count', 'return' y 'retorno_US'. </p>
**e.** Análisis gráfico (count) de las variables categóricas: 'original_language', 'status', 'production_countries_1_iso', 'genres_1_name', 'genres_2_name', 'release_year', 'belongs_to_collection_name', 'spoken_languages_1_iso' y 'Release_year'. </p>
**f.** Analisis especial a la columna release_year con el fin de poder más adelante filtrar por este concepto las películas para hacer menos pesada la data en la app. </p>
**g.** Calcula la matriz de correlación entre variables numéricas y la grafíca en un mapa de calor. </p>
**h.** Revisión de outliers.
**i** Se grafican algunas variables que son cadenas de texto en formato Nube de palabras. </p>

**3. Desarrollo Consultas:**

**4. Segunda Limpieza de Datos:**

**5. Modelo de Recomendación:**

**6. Render y FastAPI:**


 :smirk:
 :eyes:
