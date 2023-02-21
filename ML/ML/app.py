import pandas as pd
from surprise import SVDpp
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
from collections import defaultdict

movies=pd.read_csv('movies_analisis.csv')

reviews=pd.read_csv('reviews.csv')

movies=movies.drop(['show_id','cast','date_added','release_year','rating','duration_int','duration_type','scored'],axis=1)

movies = movies.reindex(columns=['Id', 'title', 'listed_in','description'])

reviews=reviews.drop(['Fecha'],axis=1)

df_movies=reviews.merge(movies, on='Id',how='left')

df_movies_to_model = df_movies[df_movies.columns[:-3]]

reader = Reader()

data = Dataset.load_from_df(df_movies_to_model[df_movies.columns[:-3]],reader)

#Separo en train y test
train, test = train_test_split(data, test_size=0.25)

#Instanciamos el algoritmo y entrenamos
svd = SVDpp()
svd.fit(train)
preds = svd.test(test)

#Métricas de evaluacin
accuracy.mae(preds)
accuracy.rmse(preds)