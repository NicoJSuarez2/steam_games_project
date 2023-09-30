# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>


## Introducción

Este proyecto final individial orientando a **"MLOps Engineer"** de la institucion en la cual me encuentro estudiando.

Para este proyecto se nos planteó el siguiente contexto:

> ### **Descripción del problema (Contexto y rol a desarrollar)**
> 
> 
> ### Rol a desarrollar
> 
> Empezaste a trabajar como **`Data Scientist`** en Steam, una plataforma multinacional de videojuegos. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: Steam pide que te encargues de crear un sistema de recomendación de videojuegos para usuarios. :worried:
> 
> Debes empezar desde 0, haciendo un trabajo rápido de **`Data Engineer`** y tener un **`MVP`** (_Minimum Viable Product_) para el fin de la semana!
> 
> ### **Propuesta de trabajo (requerimientos de aprobación)**
> 
> **`Transformaciones`**:  Para este MVP no se te pide transformaciones de datos(` aunque encuentres una motivo para hacerlo `) pero trabajaremos en leer el dataset con el formato correcto. Puedes eliminar las columnas que no necesitan para responder las consultas o preparar los modelos de aprendizaje automático, y de esa manera optimizar el rendimiento de la API y el entrenamiento del modelo.
> 
> **`Feature Engineering`**:  En el dataset *user_reviews* se incluyen reseñas de juegos hechos por distintos usuarios. Debes crear la columna ***'sentiment_analysis'*** aplicando análisis de sentimiento con NLP con la siguiente escala: debe tomar el valor '0' si es malo, '1' si es neutral y '2' si es positivo. Esta nueva columna debe reemplazar la de user_reviews.review para facilitar el trabajo de los modelos de machine learning y el análisis de datos. De no ser posible este análisis por estar ausente la reseña escrita, debe tomar el valor de `1`.
> 
> **`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. 
> 
> + **userdata( *`User_id` : str* )**:
>     Debe devolver `cantidad` de dinero gastado por el usuario, el `porcentaje` de recomendación en base a reviews.recommend y `cantidad de items`.
>     
> + **countreviews( *`YYYY-MM-DD` y `YYYY-MM-DD` : str* )**:
>     `Cantidad de usuarios` que realizaron reviews entre las fechas dadas y, el `porcentaje` de recomendación de los mismos en base a reviews.recommend.
> 
> + **genre( *`género` : str* )**:
>     Devuelve el `puesto` en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever. 
> 
> + **userforgenre( *`género` : str* )**:
>     `Top 5` de usuarios con más horas de juego en el género dado, con su URL y user_id.
> 
> + **developer( *`desarrollador` : str* )**:
>     `Cantidad` de items y `porcentaje` de contenido Free por año según empresa desarrolladora. 
> 
> + **sentiment_analysis( *`empresa desarrolladora` : str* )**:
>     Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. 
> 
> **`Modelo de aprendizaje automático`**: 
> Deben crear al menos **uno** de los dos sistemas de recomendación (Si se atreven a tomar el desafío, para mostrar su capacidad al equipo, ¡pueden hacer ambos!). Tu líder pide que el modelo derive obligatoriamente en un GET/POST en la API símil al siguiente formato:
> 
> Si es un sistema de recomendación item-item:
> + def **recomendacion_juego( *`id de producto`* )**:
>     Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.


---


# Solucion Propuesta

### Para la realizacion de este proyecto se utilizaron las siguientes herramientas:

+ **Visual Studio Code**: 
   Se utilizo como editor de codigo y generador de virtual enviroments. 

+ **Python**:
   Lenguaje de programacion utilizado en el proyecto.

+ **Jupyter Notebooks**:
   Entorno utilizado para la organizacion, del proyecyo.

+ **Pandas**: 
   Libreria de Python utilizada para el analisis, la transformacion y el modelado de datos.

+ **Numpy**:
   Libreria utilizada para optimizar datatypes y manipulacion de modelos.

+ **NLTK**:
   Libreria para aplicar NLP (Procesamiento de lenguaje natural)

+ **Scikit-learn**: 
   Libreria para aplicar modelos de ML. En este caso, Similitud de Coseno.

+ **FastAPI**:
   Web Framework para disponibilizar la informacion a travez de requests.

+ **Google COLABS**:
   Entorno de trabajo virtual Online, se utilizo para realizar avances de manera remota.

+ **Render**:
   Para realizar hacer el host de mi API de forma gratuita.

+ **GitHub**:
   Para realizar control de versiones y disponibilizar mi repositorio a Render.


### Para la realizacion de este proyecto:

- 












































# Utilizacion de la API

## Requisitos

- Python 3.7 o superior

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las bibliotecas requeridas utilizando `pip install -r requirements.txt`.
3. Asegúrate de tener los archivos de datos en la carpeta `data_api` (user_data.csv, count_reviews.csv, genre.csv, userforgenre.csv, developer.csv, sentiment_analysis.csv).
4. Ejecuta la API utilizando `uvicorn main:app --reload` desde la línea de comandos.

## Uso

### Funciones de la API

1. **/userdata/{User_id}**: Devuelve información sobre un usuario específico, incluyendo el dinero gastado, el porcentaje de recomendaciones positivas y la cantidad de juegos en su librería.

   Ejemplo de solicitud:

GET /userdata/{User_id}

2. **/countreviews/countreviewss**: Devuelve la cantidad de usuarios que realizaron reseñas entre dos fechas especificadas y el porcentaje de recomendación promedio de esas reseñas.

Ejemplo de solicitud:

GET /countreviews/countreviewss?fecha1={fecha1}&fecha2={fecha2}

3. **/genres/{Genero}**: Obtiene información sobre un género específico, incluyendo su posición en el ranking y el total de horas registradas.

Ejemplo de solicitud:

GET /genres/{Genero}


5. **/developer/{dev}**: Proporciona información sobre la cantidad de elementos y el porcentaje de contenido gratuito por año para una empresa desarrolladora específica.

Ejemplo de solicitud:

GET /developer/{dev}

6. **/sentiment_analisis/{anio}**: Devuelve la cantidad de reseñas de usuarios categorizadas con análisis de sentimiento para un año de lanzamiento específico.

Ejemplo de solicitud:

GET /sentiment_analisis/{anio}

7. **/recommend/{id_producto}**: Utiliza un algoritmo de similitud para recomendar 5 juegos distintos basados en el ID de un juego favorito.

Ejemplo de solicitud:

GET /recommend/{id_producto}



