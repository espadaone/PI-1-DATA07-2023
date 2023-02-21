import numpy as np
import pandas as pd
import pandasql as ps
from pandasql import sqldf
import gradio as gr

def get_max_season(anio:int,platform:str,duration_type:str):
    movies_complete=pd.read_csv('movies_analisis.csv')
    plat=''
    if platform=="disney":
        plat=='d%'
    elif platform=="netflix":
        plat=='n%' 
    elif platform=="amazon":
        plat=='a%'
    elif platform=="hulu":
        plat=='h%'
    else:
        return ('Recuerde escribir hulu, amazon, netflix o disney')      
    filter = (movies_complete['Id'].str.contains(plat)) & (movies_complete['release_year']==anio) & (movies_complete['duration_type']==duration_type)
    max_value=movies_complete.loc[filter,'duration_int'].max()
        
    return max_value
    

def get_score_count(platform:str, scored:float, year:int):
    movies_complete=pd.read_csv('movies_analisis.csv')    
    plat=''
    if platform=="disney":
        plat=='d%'
    elif platform=="netflix":
        plat=='n%' 
    elif platform=="amazon":
        plat=='a%'
    elif platform=="hulu":
        plat=='h%'
    else:
        return ('Recuerde escribir hulu, amazon, netflix o disney')      
    filter = (movies_complete['Id'].str.contains(plat)) & (movies_complete['scored'] > scored) & (movies_complete['release_year']==year)
    scored_value=movies_complete.loc[filter,'scored'].value_counts().reindex()
    total = scored_value.shape[0]
    
    return total

def get_count_platform(platform:str):
    movies_complete=pd.read_csv('movies_analisis.csv')
    plat=''
    if platform=="disney":
        plat=='d%'
    elif platform=="netflix":
        plat=='n%' 
    elif platform=="amazon":
        plat=='a%'
    elif platform=="hulu":
        plat=='h%'
    else:
        return ('Recuerde escribir hulu, amazon, netflix o disney') 
    filter_count= (movies_complete['Id'].str.contains(plat)).count()
    count=filter_count
        
    return count

def get_actor(platform:str, year:int):
    
    movies_complete=pd.read_csv('movies_complete.csv')
    
    plat=''
    if platform=="disney":
        plat=='d%'
    elif platform=="netflix":
        plat=='n%' 
    elif platform=="amazon":
        plat=='a%'
    elif platform=="hulu":
        plat=='h%'
    else:
        return ('Recuerde escribir hulu, amazon, netflix o disney')
    
    #count_actors = df_merge['cast'].value_counts()
    filter = (movies_complete['Id'].str.contains(plat)) & (movies_complete['release_year']==year)
    count_actors=movies_complete.loc[filter,'cast'].value_counts()
    #the_most_frecuent_actor = count_actors.index[0]
    the_most_frecuent_actor = count_actors.index[0]
    if the_most_frecuent_actor=='1':
        return count_actors.index[1]
    else:
        return the_most_frecuent_actor

with gr.Blocks() as demo:
    gr.Markdown("get_max_season or get_score_count.")
    with gr.Tab("get_max_season"):
        number_inputuno= gr.Number()
        text_inputuno = gr.Textbox()
        text_inputdos = gr.Textbox()
        number_output = gr.Number()
        text_button = gr.Button("Flips")
    with gr.Tab("get_score_count"):
        text_input = gr.Textbox()
        number_input= gr.Number()
        number_inputdos= gr.Number()
        number_outputdos = gr.Number()
        text_buttondos = gr.Button("Flip")
    with gr.Tab("get_count_platform"):
        text_inputres = gr.Textbox()
        number_outputres = gr.Number()
        text_buttontres = gr.Button("Flip")
    with gr.Tab("get_actor"):
        text_inputcuatro = gr.Textbox()
        number_inputcuatro= gr.Number()
        text_outcuatro= gr.Textbox()
        text_buttoncuatro = gr.Button("Flip")

    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")

    text_button.click(get_max_season, inputs=[number_inputuno,text_inputuno,text_inputdos], outputs=number_output)
    text_buttondos.click(get_score_count, inputs=[text_input,number_input,number_inputdos] , outputs=number_outputdos)
    text_buttontres.click(get_count_platform, inputs=text_inputres, outputs=number_outputres)
    text_buttoncuatro.click(get_actor, inputs=[text_inputcuatro,number_inputcuatro], outputs=text_outcuatro)

demo.launch()
