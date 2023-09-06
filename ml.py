import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
cv = CountVectorizer(max_features=45, stop_words="english")

df_ML_reduced = pd.read_csv(r"data_api\datos_ML_reduced.csv")
df_ML = pd.read_csv(r"data_api\datos_ML.csv")


#esta es la funcion con la que implementariamos el modelo, como vemo hacer unas recomendaciones bastantes acertadas sin caer en la reduncancia.
#dentro de los try y except no se puede llamar a variables externas a la funcion por o que me veo forzado a correr siempre la carga del modelo.
def recommend(id_item):
    #como usamos un modelo preentrenado, para una parte de los juegos la recomendacion va a ser casi instantanea.
    #para otros juegos tarda, por que tenemos que volver a entrenar el modelo.
    try:
        #cargamos el df dentro de la funcion 
        df_ML_reduced = pd.read_csv(r"data_api\datos_ML_reduced.csv")
        #importamos el modelo ya entrenado
        similarity = joblib.load('modelo_entrenado.pkl')
        #buscamos el numero de indice
        idx = df_ML_reduced[df_ML_reduced["item_id"] == id_item].index[0]
        #y lo comparamos dentro del modelo
        distances = similarity[idx]
        #determinamos nuestras similitudes mas grandes y lo guardamos dentro de una lista   
        jueguito = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]
        #guardamos dentro de una lista con este iterador las recomendaciones
        respon = []
        for i in jueguito:
            respon.append(df_ML_reduced.iloc[i[0]].title)
        return {"recomendaciones": respon}
    
    
    except IndexError:    

        df_ML_reduced = pd.read_csv(r"data_api\datos_ML_reduced.csv")
        df_ML = pd.read_csv(r"data_api\datos_ML.csv")
        new_game = df_ML[df_ML["item_id"] == id_item]
        df_combined = pd.concat([df_ML,new_game])
        vectors = cv.fit_transform(df_combined["tags"]).toarray()
        similarity=cosine_similarity(vectors)
        idx = df_combined[df_combined["item_id"] == id_item].index[0]
        distances = similarity[idx]   
        jueguito = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]
        respon = []
        for i in jueguito:
            respon.append(df_combined.iloc[i[0]].title)
        return {"recomendaciones": respon}
    
    
#print(type(recommend(10)))

            
