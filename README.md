# PI-1-DATA07-2023- Sistema de Recomendacion de Peliculas
En este proyecto se plantean dos una API de funciones que colocando lo pedido te devuelve por ejemplo 
por duracion cuanto es en minutos o temporadas. 
El otro proyecto de ML te devuelve ante un usuario determinado y una pelicula dada si es recomendable o no.

Esta carpeta se subdivide en la que contiene API de funciones que devuelven segun las consignas de pedidos de scores, tiempo max, etc y en la de ML 
En las mismas estan los parametros y requerimientos subidos para el desarrollo de los dos proyectos junto con sus CSV que se tuvieron en cuenta.
Tambien se uso 
https://huggingface.co
y Gradio
https://gradio.app/demos/
en esta misma rama del proyecto tambien se encuentra notebook del proyecto de mantenimiento de datos y el desarrollo de las funciones de la API 
Tambien esta el analisis exploratorio EDA que figura mas arriba donde tenemos distintos tipos de imagenes y de graficas que nos da las herramientas de pandas luego de haber tratado los datos. 

EN ESTE PROYECTO SE TUVIERON EN CUENTA LAS SIGUIENTES CONSIGNAS:

Propuesta de trabajo (requerimientos de aprobación)
Transformaciones: Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, y solo estas, transformaciones a los datos:

Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

De haber fechas, deberán tener el formato AAAA-mm-dd

Los campos de texto deberán estar en minúsculas, sin excepciones

El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)


Desarrollo API: Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:

Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


Deployment: Tus compañeros cercanos han usado Deta para hacer el deployment de aplicaciones, además, no necesita dockerizacion así que es el primer candidato que encuentras!

Tambien sabes sobre Railway y Render , aunque estos necesitan dockerizacion #Decisiones 👀


Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente 👀 ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Sabes que puedes apoyarte en librerías como pandas profiling, sweetviz, autoviz, entre otros y sacar de allí tus conclusiones 😉

Sistema de recomendación:

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendación debe ser deployado para tener una interfaz gráfica amigable para ser utilizada, utilizando Gradio o Deta Space para su deployment o bien con alguna solución como Streamlit o algo similar en local (tener el deployment del sistema de recomendación o una interfaz gráfica es un plus al proyecto).


Video: Sabes que la documentacion es una etapa importante en cualquier trabajo 👀. Hiciste diversos procesos nuevos para la empresa y no tienes tiempo de dejar un informe con toda la informacion relevante en este momento! Pero eres recursivo 🙂, asi que grabas un video donde muestras todo lo que hiciste para mostrarselo a tu equipo y asi tod@s pueden enteder todo lo que hiciste y para que lo hiciste.
