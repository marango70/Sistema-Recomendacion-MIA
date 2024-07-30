
# Librerias
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import datetime as dt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Instancio la App de FastAPI
app = FastAPI()

# Función que carga los datos desde un archivo Parquet
def cargar_datos():
    df = pd.read_parquet('data_movies.parquet',engine='fastparquet')
    df_credits = pd.read_parquet('data_credits.parquet', engine='fastparquet')
    return df, df_credits

#Cargo los Datos
peliculas, creditos = cargar_datos()


# 1ra consulta: "Cantidad de Filmaciones por mes"

#Le defino el decorador:
@app.get("/cantidad_filmaciones_mes")

#Consulta:
async def cantidad_filmaciones_mes(mes: str):
    mes = mes.lower()
    meses = {
        'enero': '01',
        'febrero': '02',
        'marzo': '03',
        'abril': '04',
        'mayo': '05',
        'junio': '06',
        'julio': '07',
        'agosto': '08',
        'septiembre': '09',
        'octubre': '10',
        'noviembre': '11',
        'diciembre': '12'
    }   #Diccionario con los meses en texto en español y numero de 2 digitos
    
    if mes not in meses:
        raise HTTPException(status_code=400, detail="Mes no válido")        #Si el valor de la variable mes no esta en el diccionario me saca error
    
    mes_num = meses[mes]
    
    try:
        peliculas['release_date'] = pd.to_datetime(peliculas['release_date'], errors='coerce') #Convierto la columna release_date a fecha (datetime)
        peliculas['release_month'] = peliculas['release_date'].dt.strftime('%m') #Extraigo el mes a la columna release_month
        conteo_peliculas_por_año = peliculas[peliculas['release_month'] == mes_num]['release_year'].value_counts().sort_index()
    except Exception as e:          #Manejo de escepciones
        raise HTTPException(status_code=500, detail=str(e))
    
    resultado = conteo_peliculas_por_año.to_dict()      #El resultado se almacena en un diccionario: Año:Cantidad
    return {"total_filmaciones_por_año": resultado}

# 2da Consulta: Cantidad de filmaciones por dia de la semana

#Asigno decorador
@app.get("/cantidad_filmaciones_dia")

#Consulta Cantidad de Filmaciones pordia de la semana

async def cantidad_filmaciones_dia(dia: str):
    dia = dia.lower()
    dias = {
        'lunes': 'Monday',
        'martes': 'Tuesday',
        'miércoles': 'Wednesday',
        'miercoles': 'Wednesday',
        'jueves': 'Thursday',
        'viernes': 'Friday',
        'sábado': 'Saturday',
        'sabado': 'Saturday',
        'domingo': 'Sunday'
    }       #Diccionario con los dias de la semana en español e ingles
    
    if dia not in dias:
        raise HTTPException(status_code=400, detail="Día no válido")    #Si no encuentra el dia sale error
    
    dia_str = dias[dia]
    
    try:
        peliculas['release_date'] = pd.to_datetime(peliculas['release_date'], errors='coerce')  # Convierto la columna release_date a fecha (datetime)
        peliculas['release_day'] = peliculas['release_date'].dt.day_name()  # Extrae el nombre del día de la semana
        conteo_peliculas_por_dia = peliculas[peliculas['release_day'] == dia_str].shape[0]  # Cuenta el número de películas lanzadas en el día dado
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))     #Manejo de la escepción
    
    return {"dia de la semana:": dia,
            "total_filmaciones_por_dia":  conteo_peliculas_por_dia}


#Consulta: Score por título

#Defino decorador
@app.get("/score_titulo")

#Consulta
async def score_titulo(titulo_de_la_filmacion: str):
    
    titulo_de_la_filmacion = titulo_de_la_filmacion.lower().strip()
    
    try:
        # Buscar la película por título
        pelicula = peliculas[peliculas['title'].str.lower() == titulo_de_la_filmacion]
        
        if pelicula.empty:
            raise HTTPException(status_code=404, detail="Película no encontrada")
        else:
            # Extraer los detalles de la película
            pelicula = pelicula.iloc[0]  # Toma la línea
            titulo = pelicula['title']
            anio = int(pelicula['release_year'])#Año
            score = round(float(pelicula['popularity']),2) #score
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    
    return {
        "titulo": titulo,
        "año": anio,
        "score": score
    }

#Consulta: nombre del actor

# Decorador:
@app.get("/get_actor")

async def get_actor(actor):

    actor = actor.lower().strip()

    #Lista de las columnas a buscar el actor
    columnas = ['cast_name',
                'cast_name_2',
                'cast_name_3',
                'cast_name_4'
                ] 
        
    try:
        # Buscar la película por título
        columnas_actor = creditos.apply(
                                        lambda row: any(actor in str(row[col]).lower() for col in columnas if pd.notnull(row[col])), axis=1)
        
        actor_e = creditos[columnas_actor]
        print(f"actor_e: {actor_e}")  # Log de depuración

        if actor_e.empty:
            raise HTTPException(status_code=404, detail="Actor no encontrado")
        
        # Obtener los ids de las películas
        movie_ids = actor_e['id'].unique()
        print(f"movie_ids: {movie_ids}")  # Log de depuración

        # Filtrar las películas por los ids encontrados
        peliculas_actor = peliculas[peliculas['id'].isin(movie_ids)]
        print(f"peliculas_actor: {peliculas_actor}")  # Log de depuración
        
        if peliculas_actor.empty:
            raise HTTPException(status_code=404, detail="No se encontraron películas para este actor")

        # Calcular la cantidad de películas, el retorno total y el promedio de retorno
        cantidad_peliculas = int(peliculas_actor.shape[0])
        retorno_total = float(peliculas_actor['retorno_US'].sum())
        retorno_promedio = round(float(peliculas_actor['return'].mean()),2)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

    return {
        'actor' : actor,
        'cantidad_peliculas' :cantidad_peliculas,
        'retorno_total': retorno_total,
        'retorno_promedio': retorno_promedio
    }
    
#Consulta: Director

class MovieInfo(BaseModel):
    titulo: str
    fecha_lanzamiento: str
    retorno_peli: float
    retorno_prom: float
    presupuesto: float
    retorno: float

# Decorador:
@app.get("/get_director")

async def get_director(director):

    director = director.lower().strip()

    #Lista de las columnas a buscar el actor
    columnas = ['director'] 
        
    try:
        # Buscar la película por título
        columna_director = creditos.apply(
                                        lambda row: any(director in str(row[col]).lower() for col in columnas if pd.notnull(row[col])), axis=1)
        
        director_e = creditos[columna_director]
        print(f"director_e: {director_e}")  # Log de depuración

        if director_e.empty:
            raise HTTPException(status_code=404, detail="Director no encontrado")
        
        # Obtener los ids de las películas
        movie_ids = director_e['id'].unique()
        print(f"movie_ids: {movie_ids}")  # Log de depuración

        # Filtrar las películas por los ids encontrados
        peliculas_director = peliculas[peliculas['id'].isin(movie_ids)]
        print(f"peliculas_director: {peliculas_director}")  # Log de depuración
        
        if peliculas_director.empty:
            raise HTTPException(status_code=404, detail="No se encontraron películas para este director")

        # Calcular la cantidad de películas, el retorno total y el promedio de retorno
        cantidad_peliculas = int(peliculas_director.shape[0])
        retorno_total = float(peliculas_director['retorno_US'].sum())
        retorno_promedio = round(float(peliculas_director['return'].mean()),2)

        lista_peliculas = []       
        

        for _, row in peliculas_director.iterrows():
            lista_peliculas.append(MovieInfo(
                titulo = row['title'],
                fecha_lanzamiento = row['release_date'],
                retorno_peli = row['retorno_US'],
                retorno_prom = row['return'],
                presupuesto = row['budget'],
                retorno = row['revenue']
            ))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

    return {
        'director' : director,
        'cantidad_peliculas' :cantidad_peliculas,
        'retorno_total': retorno_total,
        'retorno_promedio': retorno_promedio,
        'Información de las Películas': lista_peliculas
    }
    
# Consulta Votos por Título:

#Decorador_
@app.get("/votos_titulo")

#Consulta

async def votos_titulo(titulo_filmacion: str):
    
    titulo_filmacion = titulo_filmacion.lower().strip()
    print('Titulo de la Fimación',titulo_filmacion)  # Log de depuración

    try:
        # Buscar la película por título
        pelicula = peliculas[peliculas['title'].str.lower() == titulo_filmacion]
        
        if pelicula.empty:
            raise HTTPException(status_code=404, detail="Película no encontrada")
        
        # Extraer los detalles de la película
        pelicula = pelicula.iloc[0]  # Toma la línea

        titulo = pelicula['title']
        votos = pelicula['vote_count']
        prom_votos = pelicula['vote_average']

        if votos < 2000:
            return {"mensaje": "La película tiene menos de 2000 votos, por tanto no se devuelve ningún valor"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    
    return {
        "titulo": titulo,
        "votos": votos,
        "votos_promedio": prom_votos
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

# http://127.0.0.1:8000/cantidad_filmaciones_mes?mes=febrero
# http://127.0.0.1:8000/cantidad_filmaciones_dia?dia=lunes
# http://127.0.0.1:8000/score_titulo?titulo_de_la_filmacion=jumanji
# http://127.0.0.1:8000/get_actor?actor=robin%20williams
# http://127.0.0.1:8000/get_director?director=forest%20whitaker
# http://127.0.0.1:8000/votos_titulo?titulo_filmacion=mom

# uvicorn main:app --reload --port 8000
