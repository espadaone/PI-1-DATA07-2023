
import pandas as pd
from surprise import SVDpp
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy
from collections import defaultdict
from surprise import SVD



def recomendacion_pelicula(usuario, pelicula):
    # Cargar los datos de películas y calificaciones
    
    # Obtener el ID de la película
    movie_row = df_movies[df_movies['title'] == pelicula]
    
    movie_id = movie_row['Id'].values[1]
    
    #movie_id = df_movies[df_movies['title'] == pelicula]['Id'].values[1]
    
    # Hacer la predicción con el modelo para el usuario y la película
    prediction = model.predict(usuario, movie_id).est
    
    # Si la predicción es mayor que 3.5, recomendar ver la película
    if prediction >= 3.3:
        return f"Se recomienda ver {pelicula}."
    else:
        return f"no se recomienda ver la {pelicula}."
    
recomendacion_pelicula(usuario=2, pelicula='silent night')