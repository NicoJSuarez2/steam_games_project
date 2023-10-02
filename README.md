# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>


## Introducción
Este proyecto final individual se enfoca en la posición de **"MLOps Engineer"**en la institución en la que actualmente estoy estudiando.

Para este proyecto, se nos presentó el siguiente contexto:

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

- **main.py** : Scrip de Python donde se desarrolla la API.

- **script_ML.py** : script que se utiliza para realizar las recomendaciones.

- **modelo_entrenado.pkl** : Modelo de recomendacion entrenado en base a los mejores juegos de steam.

---

## En el desarrollo del proyecto se realizará de la siguiente manera:


- ### **Objetivos y alcances**: 

El presente proyecto tiene como objetivo la realización de un MVP (Producto Mínimo Viable) siguiendo las pautas de evaluación proporcionadas. La ejecución del mismo se llevará a cabo en un plazo de 5 días, durante los cuales se buscará aprovechar al máximo las directrices entregadas, sin perder de vista el espíritu que representa un MVP.

Como punto de partida del proyecto, se proporcionan a cada estudiante 3 archivos JSON que contienen información sobre STEAM. No se suministra un diccionario de datos. Tampoco se proporciona una guía, por lo que queda a disposición de cada desarrollador trazar la hoja de ruta del proyecto.

Es importante mencionar que se considera como un punto adicional el despliegue de la API con todos sus endpoints, así como la implementación del modelo de recomendación en la plataforma de alojamiento "render.com". Esta plataforma ofrece un servicio gratuito que consta de un servidor con 512Mb de RAM y la disponibilidad de 0.1 CPU. Dado que este servidor tiene recursos limitados, asumo como un desafío personal la optimización de cada endpoint para que la respuesta a cada solicitud sea aceptable.

- ### **EDA**:
###### Puede seguirlo en el archivo EDA.ipynb

Este EDA se centrará principalmente en evaluar la calidad de los datos proporcionados. Su objetivo principal es la exploración desde un enfoque técnico. Lo primero que se observa es que ninguno de los conjuntos de datos está en condiciones de ser utilizado, por lo que la primera tarea que propongo es llevar a cabo transformaciones en varias etapas.

La primera etapa se centrará en desanidar los diccionarios presentes en dos de los tres conjuntos de datos, colocando cada categoría en su respectiva columna y, finalmente, exportando estos datos a un formato más manejable.
![(INSERTAR IMAGEN EDA 1)](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/EDA%201.jpg)

La segunda etapa se enfocará en verificar la integridad de los datos. Para lograrlo, he creado y empleado una función que me permite analizar las columnas por separado, identificar la cantidad de valores nulos y determinar el porcentaje que representan con respecto al total de los datos.

![(INSERTAR IMAGEN EDA 2)](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/EDA%202.jpg)

El objetivo que se busca alcanzar en esta etapa es la imputación de todos los valores faltantes utilizando criterios que pueden incluir el uso de imputadores, conocimiento del negocio, entre otros. El propósito es evitar la pérdida de información que pueda ser relevante, eliminando solo aquellos registros que no sean susceptibles de imputación, y finalizar con cada DataFrame sin ningún valor nulo. Este trabajo se puede ver en *EDA.ipynb*.

Dentro de esta etapa, se llevó a cabo el "feature engineering", en la cual se transformó el texto de las reseñas en un valor "compound", donde -1 representa una polaridad negativa absoluta, 0 indica neutralidad y 1 denota una polaridad positiva. Para llevar a cabo esta tarea, se empleó el modelo VADER. La elección de este modelo se debió a su simplicidad de aplicación y su bajo costo computacional. También se consideró el uso del modelo RoBERTa, el cual trabaja con otras bibliotecas de Machine Learning como PyTorch. Sin embargo, en el momento de la realización de este proyecto, carecíamos de las herramientas estructurales necesarias para su implementación, ya que estas bibliotecas de Deep Learning requieren el uso de una tecnología llamada CUDA, la cual está disponible solo en las GPUs de Nvidia.


- ### **Expicación API**:
###### Puede seguirlo en el archivo Dataframes_API.ipynb

Una vez completada la etapa anterior, con cada conjunto de datos limpio y listo para su uso, el siguiente paso implica analizar cómo se desarrollará la API. En primer lugar, debemos tener en cuenta las limitaciones del servicio de alojamiento proporcionado. Con el objetivo de reducir la carga en el servidor en la nube, mi enfoque es simplificar al máximo las consultas que deben realizarse en cada punto final para proporcionar la información requerida.

El mayor desafío que encontramos en esta sección es abastecer el primer punto final de la API, para lo cual se requieren los tres dataframes.


> **userdata( *`User_id` : str* )**:
>     Debe devolver `cantidad` de dinero gastado por el usuario, el `porcentaje` de recomendación en base a reviews.recommend y `cantidad de items`.

Para este caso, necesitamos extraer el precio del producto de un dataframe, las recomendaciones realizadas en otro y la cantidad de ítems que tiene ese usuario en otro. Además, debemos utilizar funciones de agregación. Por un lado, esta tarea podría ocasionar varios problemas de almacenamiento, ya que sería costoso cargar constantemente todos mis archivos CSV en un dataframe de pandas (en total superan los 700MB). Además, sería extremadamente costoso en cuanto a recursos computacionales, dado que uno de ellos contiene más de 5 millones de registros. Por lo tanto, he decidido llevar a cabo todas estas operaciones de forma previa, mediante un proceso de preprocesamiento, y aplicar esta lógica para cada endpoint. 



![(INSERTAR IMAGEN API1)](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/API%201.jpg)

De esta manera, logro reducir el tamaño total de los datos de 700MB a aproximadamente 60MB, lo que garantiza respuestas inmediatas tanto en mi servicio "render" como en mi entorno local. Además, estoy simplificando enormemente el código de cada endpoint, como se puede observar, ya que prácticamente se reduce a una sola línea de código por función.

###### Puede seguirlo en el archivo main.py
![INSERTAR IMAGEN API2 ](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/API%202.jpg)


Por último, para la implementación de la API, he decidido utilizar FastAPI, ya que nos ofrece varias ventajas. Entre ellas, podemos probarla de forma local y ver los cambios en tiempo real. Además, FastAPI genera automáticamente documentación de la API y nos proporciona la posibilidad de probar cada endpoint de manera sencilla.

![INSERTAR IMAGEN API 3](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/API%203.jpg)

> *Si desea probar la API a travez de su documentacion puede hacerlo ingresando al siguiente Link:*
>
> https://steam-games-project-api.onrender.com/docs


- ### **Expicación ML**:
###### Puede seguirlo en el archivo Dataframes_API.ipynb

Para la creación del modelo de machine learning, me basé en el modelo de similitud por coseno, que es una medida de la similitud entre dos vectores en un espacio que posee un producto interior con el que se evalúa el valor del coseno del ángulo comprendido entre ellos. En otras palabras, vectorizamos las características de nuestros productos y las comparamos. En nuestro caso, utilizamos dos dataframes distintos: uno que contiene las reviews de los juegos y otro que contiene la información de los juegos en sí.

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


Para la realización de este modelo, puede seguir el proceso detallado en el archivo **desarrollo_ML.ipynb**.

Utilizamos un dataframe que contiene los registros de los 2000 juegos con las mejores puntuaciones. Esto nos permite abordar dos cuestiones importantes:

- **Evitar recomendar juegos que son considerados malos por la comunidad de usuarios**, lo que podría afectar negativamente la experiencia del usuario.usuraio.
- **Eficientizar el costo computacional y de almacenamiento de nuestro servidor en línea**. Preentrenar nuestro modelo nos permite evitar costos adicionales en ciertos casos.

La similitud de coseno convierte las listas de palabras clave en vectores. Cada juego se representa como un vector en un espacio multidimensional, donde cada dimensión corresponde a una palabra clave (columna "tags"). Los valores en el vector indican cuán importante es cada palabra clave para ese juego.

Este algoritmo calcula el coseno del ángulo entre los vectores de dos juegos. Si el coseno es 1, significa que son idénticos; si es 0, no tienen similitud; y si es -1, son completamente opuestos.

Para la implementación de este modelo, se tuvieron en cuenta varios hiperparámetros, pero dos de los más importantes fueron:
- **La cantidad de registros utilizados para entrenar el modelo** Se limitó a 2000 registros, lo que nos permitió enfocarnos en juegos que mejor puntuacion de score tengan y al mismo tiempo reducir costos computacionales y de almacenamiento.
- **La cantidad de características (features) consideradas para las recomendaciones:**  Se mantuvo en 45 características. Esta elección permite recomendar juegos que están relacionados lo suficiente con el juego original, pero evita redundancias, como recomendar secuelas del mismo juego. Esto se debe a que es probable que los usuarios que buscan recomendaciones de un juego ya conozcan sus secuelas.

Por supuesto, es una buena práctica estar abierto a la optimización de hiperparámetros en el futuro, especialmente después de que el modelo haya sido probado con el público en general. La optimización de hiperparámetros puede ayudar a mejorar el rendimiento y la precisión del modelo a medida que se obtienen más datos y retroalimentación de los usuarios. Mantener un enfoque de mejora continua es esencial para asegurarse de que el modelo de recomendación siga siendo eficaz y relevante con el tiempo.

![INSERTAR ML 5](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/ML%205.jpg)

Es inteligente considerar estos dos escenarios al diseñar tu API de recomendación. Esto te permite manejar eficientemente la búsqueda de recomendaciones según la disponibilidad de un ID en el modelo original:

- **El ID ingresado está dentro de nuestro modelo originario:** En este caso, la respuesta es automática y eficiente, ya que no difiere de buscar las recomendaciones en un dataframe con todas las posibilidades. Esto reduce el costo computacional a una simple consulta, lo que es óptimo para el rendimiento de la API.

- **El ID ingresado no está dentro de nuestro modelo originario:** Aquí suponemos que el usuario ha ingresado un ID que no estaba contemplado en el modelo original. Como resultado, el modelo no tiene información previamente calculada para este ID, lo que requiere la realización del cálculo completo. Aunque esto puede ser más costoso en términos de recursos computacionales, es necesario para manejar nuevos casos y proporcionar recomendaciones incluso para elementos no previstos en el modelo original.

Esta estrategia te permite equilibrar el rendimiento y la capacidad de adaptación de tu API, atendiendo tanto a casos predefinidos como a situaciones inesperadas.

![INSERTAR ML 5](https://github.com/gomezgaston/steam_games_project/blob/main/imagenes/ML%204.jpg)



**Aviso Importante:** 
Por cuestiones de tiempo, debido a que este proyecto tenía un plazo de ejecución limitado a 5 días, no se han implementado procesos de verificación de datos ingresados a los endpoints de la API. La API funciona de manera óptima cuando el usuario ingresa los datos exactamente como se requieren.


---

---

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



