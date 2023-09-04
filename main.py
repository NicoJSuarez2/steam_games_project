from fastapi import FastAPI
import pandas as pd
df_userdata = pd.read_csv(r"data_api/user_data.csv",index_col=0)
df_countreviews = pd.read_csv(r"data_api/count_reviews.csv",index_col=0)
df_genre = pd.read_csv(r"data_api/genre.csv")
df_userforgenre = pd.read_csv(r"data_api/userforgenre.csv",index_col=0)
df_developer = pd.read_csv(r"data_api/developer.csv",index_col=0)
df_sentiment_analysis = pd.read_csv(r"data_api/sentiment_analysis.csv")
df_ML = pd.read_csv(r"data_api\datos_ML.csv", index_col=False)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=200, stop_words="english")
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
ps = PorterStemmer()
    
app = FastAPI()

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)
vectors = cv.fit_transform(df_ML["tags"]).toarray()
df_ML["tags"] = df_ML["tags"].apply(stem)
similarity =  cosine_similarity(vectors)


cosine_similarity(vectors)

@app.get("/userdata/{User_id}")
def userdata(User_id:str):
    '''
    Devuelve la cantidad de dinero gastado por el usuario ingresado, el porcentaje de 
    recomendaciones que dejo y cuantos juegos comprados tiene en su libreria.
    '''
    
    filtered_df = df_userdata.query(f"user_id == '{User_id}'")
    response= {"Usuario_ingresado":str(filtered_df.iloc[0,0]),
            "Dinero_Gastado":int(filtered_df.iloc[0,2]),
            "Porcentaje de recomendaciones hechas positivas":float(filtered_df.iloc[0,3]),
            "Cantidad de Juegos en libreria":int(filtered_df.iloc[0,1])}
    return response

@app.get("/countreviews/countreviewss")
def countreviews(fecha1,fecha2 : str):
    '''
    Devuelve la cantidad de usuarios que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación de los mismos.
    '''
    
    df_countreviews["posted"] = pd.to_datetime(df_countreviews["posted"])
    fecha1 = pd.to_datetime(fecha1)
    fecha2 = pd.to_datetime(fecha2)
    df_filtered = df_countreviews[df_countreviews['posted'].between(f"{fecha1}", f"{fecha2}")]
    response = {"Cantidad de usuarios que hicieron reviews": str(df_filtered["sum_review"].sum()),
                "Porcentaje de recomendacion de reviews" : str(df_filtered["recommend_percentage"].mean())}
    return response

@app.get("/genres/{Genero}")
def genre(Genero:str):
    '''
    Devuelve el puesto en el que se encuentra un género sobre el ranking de los generos mas jugados de steam.
    Los diferentes generos son:
    
    Action
    Adventure
    Animation and Modeling
    Audio Production
    Casual
    Design and Illustration
    Early Access
    Education
    Free to Play
    Indie
    Massively Multiplayer
    Photo Editing
    RPG
    Racing
    Simulation
    Software Training
    Sports
    Strategy
    Utilities
    Video Production
    Web Publishing

    
    '''
    filtered_df = df_genre.query(f"genres == '{Genero}'")
    response = {"Genero":str(filtered_df.iloc[0,0]),
                "Posicion en el Top":str(filtered_df.iloc[0,2]),
                "Total de horas registradas":int(filtered_df.iloc[0,1])}
    return response

@app.get("/userforgenre/{Genero}")
def userforgenre(Genero:str):
    '''
    Devuelve el `Top 5` de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.
    Los diferentes generos son:
    
    Action
    Adventure
    Animation and Modeling
    Audio Production
    Casual
    Design and Illustration
    Early Access
    Education
    Free to Play
    Indie
    Massively Multiplayer
    Photo Editing
    RPG
    Racing
    Simulation
    Software Training
    Sports
    Strategy
    Utilities
    Video Production
    Web Publishing
    
    '''
    
    filtered_df = df_userforgenre.query(f"genres == '{Genero}'").sort_values(by= "playtime_forever", ascending=False).head(5)
    
    user_info_list = filtered_df.to_dict(orient='records')

    return user_info_list


@app.get("/developer/{dev}")
def developer(dev:str):
    '''
    Devuelve `Cantidad` de items y `porcentaje` de contenido Free por año según empresa desarrolladora.
    '''
    filtered_df = df_developer.query(f"developer == '{dev}'")
    
    return filtered_df.sort_values(by='release_date', ascending=False).to_dict(orient='records')

@app.get("/sentiment_analisis/{anio}")
def sentiment_analysis(anio: int):
    '''
     Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
    '''
    filtered_df = df_sentiment_analysis.query(f"release_date == '{anio}'")
    response = {'Año de lanzamiento' : int(filtered_df.iloc[0,0]),
                'Reseñas Negativas' : int(filtered_df.iloc[0,1]),
                'Reseñas Neutras' : int(filtered_df.iloc[0,2]),
                'Reseñas Positivas' : int(filtered_df.iloc[0,3])}
    return response



@app.get("/recomendacion_juego/{id_producto}")
def recommend(id_jueguito:int):
    '''
    Recomienda 5 juegos segun el juego que vos le digas!
    '''
    game_index = df_ML[df_ML["item_id"]==id_jueguito].index[0]
    distances = similarity[game_index]
    games_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    respon = {"tu juego es" : df_ML[df_ML["item_id"]==id_jueguito].iloc[0,1],
            "recomendaciones": []}
    for i in games_list:
        respon["recomendaciones"].append(df_ML.iloc[i[0]].title)
        
    return respon
