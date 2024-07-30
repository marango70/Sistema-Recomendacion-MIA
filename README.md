
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

1. **Limpieza de Datos:**
   En este paso se realiza el cargue y un análisis inicial de datos de los dataset movies_dataset.csv y credits.csv, con el fin de limpiarlos y prepararlos para su uso. (Ver archivo **´Data_Engineering.ipyn´**).
   </p>
   En el este notebook se carga la información de los 2 datasets: (data_movies.csv y data_credist.csv):
   </p>
   a. Se reviza de la información de los 2 datasets (Descripción, visualización de encabezados e información general y forma)</p>
   b. Elimina los duplicados presentes en el dataset movies.</p>
   c. </p>
   </p>
   b. Se eliminan las columnas cuyos valores nulos sean superiores al 50% de los datos.
   </p>
   c. Se eliminan duplicados.
   </p>
   d. Se exportan los archivos a formato .parquet para usarlos posteriormente en la API.
   </p>
2. **Analisis de Datos EDA:** Se realiza un análisis gráfico y de las características de los datos de los datasets.
   </p>
:eyes:    El código python de limpieza y análisis de datos corresponde al archivo **`Data Engineering.ipynb`**   :eyes:
</p>
Se exportan los datasets resultantes en formato .json y .parquet con en fin de evaluar posteriormente el mejor formato de trabajo.
Los archivos resultantes son:

**`data_movies.json`**
**`data_credits.json`**
**`data_movies.parquet`**
**`data_credits.parquet`**


3. 

5. 
 :smirk:
 :eyes:
 :weary:

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.


## Rol a desarrollar

 **`Data Scientist`** 
