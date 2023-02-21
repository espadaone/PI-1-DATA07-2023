import pandas as pd
import gradio as gr
import pandasql as ps
from pandasql import sqldf

def get_max_season(anio:int,platform:str,duration_type:str):      
        movies_complete=pd.read_csv('movies_complete_re.csv')
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
        text_input = gr.Number()
        text_button.click(get_max_season, inputs=(number_input,text_input,tex_input), outputs=number_output)
demo=gr.Interface((fn=get_max_season,  inputs=["number","text","text"], outputs="number")+(fn=getattr,  inputs=["number","text","text"], outputs="number"))
