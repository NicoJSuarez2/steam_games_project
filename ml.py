import pandas as pd
import joblib
df_ML = pd.read_csv(r"data_api\datos_ML.csv")
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=500, stop_words="english")
from sklearn.metrics.pairwise import cosine_similarity

df_ML = pd.read_csv(r"data_api\datos_ML.csv")
df_ML_reduced = pd.read_csv(r"data_api\datos_ML_reduced.csv")


#esta es la funcion con la que implementariamos el modelo, como vemo hacer unas recomendaciones bastantes acertadas sin caer en la reduncancia.
#dentro de los try y except no se puede llamar a variables externas a la funcion por o que me veo forzado a correr siempre la carga del modelo.
def recommend(id_jueguito):
    try:
        similarity = joblib.load('modelo_entrenado.pkl')
        idx = df_ML_reduced[df_ML_reduced["item_id"] == id_jueguito].index[0]
        distances = similarity[idx]   
        jueguito = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]
        respon = {"tu juego es" : df_ML_reduced[df_ML_reduced["item_id"]==id_jueguito].iloc[0,1],
                "recomendaciones": []}
        for i in jueguito:
            respon["recomendaciones"].append(df_ML_reduced.iloc[i[0]].title)
        
        return respon
    except IndexError:
        print("buscando recomendaciones, por favor espere")
        new_game = df_ML[df_ML["item_id"] == id_jueguito]
        df_combined = pd.concat([df_ML,new_game])
        vectors = cv.fit_transform(df_combined["tags"]).toarray()
        similarity=cosine_similarity(vectors)
        idx = df_combined[df_combined["item_id"] == id_jueguito].index[0]
        distances = similarity[idx]   
        jueguito = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]
        respon = {"tu juego es" : df_combined[df_combined["item_id"]==id_jueguito].iloc[0,1],
        "recomendaciones": []}
        for i in jueguito:
            respon["recomendaciones"].append(df_combined.iloc[i[0]].title)
            
        return respon
            
            
