from fastapi import FastAPI
import pandas as pd
import joblib
from script_ML import recommend
df_userdata = pd.read_csv(r"data_api/user_data.csv",index_col=0,low_memory=False)
df_countreviews = pd.read_csv(r"data_api/count_reviews.csv",index_col=0,low_memory=False)
df_genre = pd.read_csv(r"data_api/genre.csv",low_memory=False)
df_userforgenre = pd.read_csv(r"data_api/userforgenre.csv",index_col=0,low_memory=False)
df_developer = pd.read_csv(r"data_api/developer.csv",index_col=0,low_memory=False)  
df_sentiment_analysis = pd.read_csv(r"data_api/sentiment_analysis.csv",low_memory=False)



app = FastAPI()


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

@app.get("/countreviews/{date1}/{date2}")
def countreviews(date1,date2 : str):
    '''
    Devuelve la cantidad de usuarios que realizaron reviews entre las fechas dadas y, el porcentaje de recomendación de los mismos.
    '''
    
    df_countreviews["posted"] = pd.to_datetime(df_countreviews["posted"])
    date1 = pd.to_datetime(date1)
    date2 = pd.to_datetime(date2)
    df_filtered = df_countreviews[df_countreviews['posted'].between(f"{date1}", f"{date2}")]
    response = {"Cantidad de usuarios que hicieron reviews": str(df_filtered["sum_review"].sum()),
                "Porcentaje de recomendacion de reviews" : str(df_filtered["recommend_percentage"].mean())}
    return response

@app.get("/genres/{genre}")
def genre(genre:str):
    '''
    Devuelve el puesto en el que se encuentra un género sobre el ranking de los generos mas jugados de steam.
    Los diferentes generos son:
    
    Actionf
    
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
    filtered_df = df_genre.query(f"genres == '{genre}'")
    response = {"Genero":str(filtered_df.iloc[0,0]),
                "Posicion en el Top":str(filtered_df.iloc[0,2]),
                "Total de horas registradas":int(filtered_df.iloc[0,1])}
    return response


@app.get("/userforgenre/{genre}")
def userforgenre(genre:str):
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
    
    filtered_df = df_userforgenre.query(f"genres == '{genre}'").sort_values(by= "playtime_forever", ascending=False).head(5)
    
    user_info_list = filtered_df.to_dict(orient='records')

    return user_info_list


@app.get("/developer/{dev}")
def developer(dev:str):
    '''
    Devuelve `Cantidad` de items y `porcentaje` de contenido Free por año según empresa desarrolladora.
    '''
    filtered_df = df_developer.query(f"developer == '{dev}'")
    
    return filtered_df.sort_values(by='release_date', ascending=False).to_dict(orient='records')

@app.get("/sentiment_analisis/{year}")
def sentiment_analysis(year: int):
    '''
     Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
    '''
    filtered_df = df_sentiment_analysis.query(f"release_date == {year}")
    response = {'Año de lanzamiento' : int(filtered_df.iloc[0,0]),
                'Reseñas Negativas' : int(filtered_df.iloc[0,1]),
                'Reseñas Neutras' : int(filtered_df.iloc[0,2]),
                'Reseñas Positivas' : int(filtered_df.iloc[0,3])}
    return response


@app.get("/recommend/{id_item}")
async def get_recommendations(id_item: int):
    '''
    Algoritmo basado en coseno de similitud.
    Ingrese el id de su juego favorito y le recomendamos 5 distintos para que pruebe.
    
    '''
    return recommend(id_item)



