import streamlit as st
import pandas as pd
import numpy as np

st.title('SIMPLE VECTOR MATRIX APPS')

#untuk sidebar
with st.sidebar:
    tipe = st.radio ('pilih tipe',['single vector', 'double matrix'])

#untuk expander (memilih ukuran)
with st.expander('Pilih Ukuran'):
    with st.form('Pilih Ukuran'):
       if tipe == 'single vector':
           size = st.number_input('ukuran dari vektor', min_value=2) 
       elif tipe == 'double matrix':
           row = st.number_input('ukuran baris dari matrix pertama', min_value=2)
           col1 = st.number_input('ukuran kolom dari matrix pertama', min_value=2)
           row2 = st.number_input('ukuran baris dari matrix kedua', min_value=2)
           col2 = st.number_input('ukuran kolom dari matrix kedua', min_value=2)

       st.form_submit_button('kirim ukuran')    

#untuk input data
if tipe == 'single vector':
    st.write('data untuk vektor')
    df = pd.DataFrame(columns=range(1,size+1), index=range(1,2), dtype=float)   #untuk membuat tabel kosong
    df_input = st.experimental_data_editor(df, use_container_width=True)
    
elif tipe == 'double matrix':
    st.write('data untuk matrix pertama')
    df_1 = pd.DataFrame(columns=range(1,col1+1), index=range(1, row+1), dtype=float)   #untuk membuat tabel kosong
    df_1_input = st.experimental_data_editor(df_1, use_container_width=True, key=1)

    st.write('data untuk matrix kedua')
    df_2 = pd.DataFrame(columns=range(1,col2+1), index=range(1, row2+1), dtype=float)   #untuk membuat tabel kosong
    df_2_input = st.experimental_data_editor(df_2, use_container_width=True, key=2)

#convert table to matrix
matrix_1= df_1_input.fillna(0).to_numpy()
matrix_2= df_2_input.fillna(0).to_numpy()
operasi = st.radio ('pilih operasii', ['A*B', 'A+B'])
if operasi == 'A*B':
    hasil = np.matmul(matrix_1, matrix_2)
elif operasi == 'A+B':
    hasil=matrix_1 + matrix_2
    st.write(hasil)