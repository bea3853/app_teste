import streamlit as st
import pandas as pd
import numpy as np


dados = {

     'dia' : [1,2,3,4,5],
     'Vendas':[500,450,200,150,1000]

}

df =  pd.DataFrame(dados)
if st.button('Gerar Grafico'):
   st.line_chart(df.set_index('dia')) 


# ----------------------------------------



st.title('Ler o CSV')

arquivo = st.file_uploader('Enviar CSV', type=["csv"])

if arquivo:
   df = pd.read_csv('dado.csv')
   st.write('dados')
   st.dataframe(df['venda'])
   if st.button('gerar um grafico'):
      st.bar_chart(df['vendedor']) 


# -----------------------------


st.title('Imagem')
st.image('img.jpg', caption='teste')

url = st.text_input('insira a url da imagem')
if url:
   st.image(url, caption='image')



# mvp 