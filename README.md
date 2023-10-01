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


## Para la realizacion de este proyecto se utilizaron las siguientes herramientas:

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

+ **Joblib**:
   Para la exportacion del modelo de machine learning entrenado.

+ **Google COLABS**:
   Entorno de trabajo virtual Online, se utilizo para realizar avances de manera remota.

+ **Render**:
   Para realizar hacer el host de mi API de forma gratuita.

+ **GitHub**:
   Para realizar control de versiones y disponibilizar mi repositorio a Render.


## Para la realizacion del proyecto se disponibilizan los siguientes archivos:

- **EDA.ipynb** : Donde se realiza un analisis exploratorio y las transformaciones necesarias.

- **Dataframes_API.ipynb** : Donde se crean los dataframes especificos para alimentar cada endpoint de la API.

- **desarroto_ML.ipynb** : Donde se muestra el proceso que se siguió para la realizacion del modelo de Machine Learning

- **main.py** : Scrip de Python donde se desarroya la API.

- **script_ML.py** : script que se utiliza para realizar las recomendaciones.

- **modelo_entrenado.pkl** : Modelo de recomendacion entrenado en base a los mejores juegos de steam.

---

## En el desarroyo del proyecto se realizará de la siguiente manera:


- ### **Objetivos y alcances**: 

El siguiente proyecto tiene como objetivo la realizacion de un MVP siguiendo las rubricas de evaluacion entregadas. La realizacion del mismo se realizará en un plazo de 5 días en el que se intentará sacar el mayor provecho posible a las consignas entregadas, pero sin perder el espiritu de lo que representa un MVP. 

Como punto de partida del proyecto se entregan a cada alumna 3 archivos JSON que contienen informacion acerca de STEAM. No se entrega diccionario de datos, por lo que realizaré uno. Tampoco se entrega una posible guía por lo que queda a dispocicion de cada desarroyador la hoja ruta del proyecto. 

Es importante mensionar que se pone como punto extra el deploy de la API con todos sus endpoints y adicionalmente el modelo de sistema de recomendacion en la plataforma de host "render.com" la cual ofrece un servicio gratuito que consta de un servidor con 512Mb RAM y la disponibilidad de 0.1 CPU. Al tener un servidor de tan escasas caracteristicas, me tomo como desafio personal la optimizacion de cada endpoint de manera que la repsuesta a cada request sea aceptable. 

- ### **EDA**:
###### Puede seguirlo en el archivo EDA.ipynb

Este EDA será dirigido principalmente a encontrar la calidad de los datos que se nos entregan, tiene como objetivo principal la exploracion a un nivel tecnico. Lo primero que se nota es que todos los conjuntos de datos no estan en condiciones de ser utilizados por lo que lo primero que planteo es realizar transformaciones en etapas.

La primer etapa será dirigida a desanidar aquellos diccionarios que se encuentran en 2 de mis 3 conjuntos de datos, poniendo cada categoría en un respectiva columna y por ultimo, exportando estos datos a un formato mas trabajable. 
![(INSERTAR IMAGEN EDA 1)](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/EDA%201.jpg)

La segunda etapa será dirigida a encontrar la integridad de los datos. Para ello creo y utilizo una funcion que me permite analizar las columnas por separado, encontrar el numero de valores nulos y determinar a que porcentaje del total de los datos representan esos valores nulos.

![(INSERTAR IMAGEN EDA 2)](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/EDA%202.jpg)

El objetivo a llegar de esta etapa es el de imputar todos los valores faltantes utilizando el criterio, para esto se utiliza imputadores, conocimiento en el negocio, etc.
Se busca no perder informacion que pueda llegar a ser reelevante, solo eliminar registros que sean inumputables y finalizar con cada df con 0% de nulos. Este trabajo se puede ver en *EDA.ipynb*.

Dentro de esta etapa se realizo el "feature engineering", donde se cambio el texto de la reviews por un "compund" donde el -1 es el negativo absoluto, el 0 el neutral y el 1 el positivo. Para la realizacion de esto se utilizó el modelo VADER. La eleccion de este modelo fue debido a que es un modelo de aplicacion sencilla y no tiene mucho costo computacional. Tambien se analizó la utilizacion del modelo de RoBERTa, el cual trabaja con otras librerias de Machine Learning como PyTorch, pero al momento de la realizacion de este proyecto carecia de las herramientas estructurales necesarias para aplicarlos ya que estas librerias de Deep Learning utilizan para la realizacion de sus computos de una tecnologia llamada CUDA, disponible solo en GPUs de Nvidia.


- ### **Expicación API**:
###### Puede seguirlo en el archivo Dataframes_API.ipynb

Una vez finalizada la etapa anterior, teniendo cada dataset limpio y listo para usar, el siguiente paso es analizar como se realizará la API. Primero tenemos que tener en cuenta las limitaciones que tiene el servicio de hosting provisto. Para intentar quitarle carga al servidor en la nube, lo que intento es simplificar lo mas posible las consultar que se tenga que hacer en cada endpoint para devolver la informacion requerida. 

El mayor desafio que encontramos en este apartado es alimentar el primer endpoint de la API, para la cual se requieren los 3 dataframes. 


> **userdata( *`User_id` : str* )**:
>     Debe devolver `cantidad` de dinero gastado por el usuario, el `porcentaje` de recomendación en base a reviews.recommend y `cantidad de items`.

Para este caso necesitamos sacar el precio del producto de un dataframe, las recomendaciones que hizo de otro y la cantidad de items que tiene ese usuario de otro, aparte de usar funciones de agregacion. Por una parte, esto causaría problemas varios de almacenamiento, sería muy costoso todos mis archivos CSV en un dataframe de pandas constantemente (en total superan los 700MB) y aparte sería extremandamente costoso computacionalmente (ya que uno de ellos contiene mas de 5 millones de registros). Decido realizar todas esta operaciones de forma previa, haciendo un estilo de preprocesamiento y utilzando esta logica para cada endpoint. 



![(INSERTAR IMAGEN API1)](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/API%201.jpg)

De esta manera cosigo reducir el total de 700Mb  a aproximadamente 60Mb, y logrando una respuesta inmediata tanto en mi servicio "render" como en local. Tambien estoy simplificando extremnadamente el codigo de cada endpoint, como vemos es practicamente una sola linea de codigo por funcion. 

###### Puede seguirlo en el archivo main.py
![INSERTAR IMAGEN API2 ](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/API%202.jpg)


Por ultimo, para la realizacion de la API decido utilizar FastAPI, ya que nos da varias ventajas. Entre ellas que podemos probarla de forma local a y ver los cambios en tiempo real. Por otra parte nos genera Documentacion de la API y la posibilidad de probar cada endpoint. 

![INSERTAR IMAGEN API 3](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/API%203.jpg)

> *Si desea probar la API a travez de su documentacion puede hacerlo ingresando al siguiente Link:*
>
> https://steam-games-project-api.onrender.com/docs


- ### **Expicación ML**:
###### Puede seguirlo en el archivo Dataframes_API.ipynb

Para la creacion del modelo de machine learning me basé en el modelo de similitud por coseno que es una medida de la similitud existente entre dos vectores en un espacio que posee un producto interior con el que se evalúa el valor del coseno del ángulo comprendido entre ellos, o en palabras muy simplificadas: Vectorizamoz caracteristicas de nuestros productos y las comparamos. En nuestro caso utilizamos 2 dataframes distintos, el que hace referencia a reviews de los juegos y el de juegos en si.

Para ello, mis variables fueron:

- **Del dataframe steam_games:**
   - La columna artificial que creé para agrupar todas las caracteristicas que tiene el juego, entre "genre", "tags" y "specs".
   - El Developer.
   - El precio del juego.

![(INSERTAR ML 1)](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/ML%201.jpg)

- **Del dataframe user_reviews:**
   - Una sumatoria de la cantidad de recomendaciones que recibio el juego
   - Un promedio de los refiews (utilizando el analizador de sentimientos)
   - La combinacion de estas dos columnas a travez del "scaling" (normalizacion de variables), generandole un score.

![INSERTAR ML 2](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/ML2.jpg)

Como resultante tengo obtengo este DartaFrame:

![INSERTAR ML 3](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/ML%203.jpg)


Para la realizacion de este modelo 
###### Puede seguirlo en el archivo desarroyo_ML.ipynb

Para la realizacion del modelo se utilizó un dataframe que contenia los registros *2000* con mejor score, de esta manera  dos cuestiones:

- **Evitamos que se recomiende juegos que sean considerados malos por la comunidad de usuarios**. Esto es un escenario malo para la empresa afectando directamente la experiencia de usuraio.
- **Eficientizamos el costo computacional y de almacenamiento** de nuestro servidor online. Podemos permitirnos pre entrenar nuestro modelo y asi evitar costos adicionales en algunos supuestos.

La similitud de coseno convierte las listas de palabras clave en vectores. Cada Juego se representa como un vector en un espacio multidimensional, donde cada dimensión corresponde a una palabra clave (columna "tags"). Los valores en el vector indican cuán importante es cada palabra clave para ese juego.
Este algoritmo calcula el coseno del ángulo entre los vectores de dos juegos. Si el coseno es 1, significa que son idénticos; si es 0, no tienen similitud; y si es -1, son completamente opuestos.

Para la implementacion de este modelo se tuvieron en cuenta varios hiper-parametros, pero de todos ellos los mas importantes fueron 2: 
- **La cantidad de registros con la que se realizó el modelo,** limitandolo a 2000 para mantener juegos con buen score y tambien ahorro de costos
- **La cantidad de features que se tienen en cuenta** para realizar las recomendaciones manteniendolo en 45, de esta manera recomendamos juegos los suficientemente relacionados al original pero sin caer en la redundancia (como recomendar secuelas del mismo, ya que lo mas probable es que el usuario si esta buscando resomendaciones de un juego, ya conozca de la existencia de las misma)

De todas maneras siempre se esta abierto a optimizar hiperparametros en el futuro, una vez testeado el modelo con el publico genenal.


![INSERTAR ML 5](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/ML%205.jpg)

Teniendo en cuenta las limitaciones que tiene el host de nuestra API, se tuvieron en cuenta 2 posibles escenarios:

- **El Id ingresado esta dentro de nuestro modelo originario.** En tal caso la respuesta sería automatica y no sería distinto de buscar las recomendaciones en un dataframe con todas las posibilidades. Sería el caso ideal en el que el costo computacional se veria reducido a una simple consulta

- **El Id ingresado no esta dentro de nuestro modelo originario.** En este caso suponemos que el usuario ingresa in Id que no teniamos contemplado en el modelo por lo que al no encontrarlo en nuestro modelo ya entrenado, nos vemos forzados a la realizacion del calculo completo.
![INSERTAR ML 5](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/ML%204.jpg)



- **Conclusiones** :




# Utilizacion de la API

## Requisitos

- Python 3.7 o superior

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las bibliotecas requeridas utilizando `pip install -r requirements.txt`.
3. Asegúrate de tener los archivos de datos en la carpeta `data_api` (user_data.csv, count_reviews.csv, genre.csv, userforgenre.csv, developer.csv, sentiment_analysis.csv).
4. Ejecuta la API utilizando `uvicorn main:app --reload` desde la línea de comandos.
5. Tambien puede consumir esta api utilizando el siguiente link https://steam-games-project-api.onrender.com/


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



