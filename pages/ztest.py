import streamlit as st
import pandas as pd
from statistics import NormalDist
from statsmodels.stats.weightstats import ztest
from scipy.stats import shapiro

st.title('ZTEST')
with st.expander('view data'):
    df= pd.read_csv('https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv')
    st.dataframe(df.transpose())

with st.expander('view statistics'):
    st.dataframe(df.describe().transpose()) 

st.write('## Constructing Hypothesis')
st.latex('H_{0}: \mu = \mu_{0}')
st.latex('H_{1}: \mu \ne \mu_{0}')

alpha = st.number_input(f'masukkan nilai alpha', min_value=0.001, max_value=0.999)
null_mean = st.number_input('masukkan nilai mu_0')
clicked = st.button('do the Z test!!')

if clicked:
    print('DEBUG', alpha)
    alpha_z= NormalDist().inv_cdf(p=1-alpha/2)
    z_score, p_value = ztest(df['grades'], value=null_mean, alternative='two-sided')

if clicked:
    if abs(z_score) > alpha_z:
        st.latex('REJECT H_{0}')    
    else:
        st.latex('CAN  NOT REJECT H_{0}')
    st.write(f'titik kritis = {alpha_z}, hitung z = {z_score}, p_value = {p_value}')    
    #st.latex(f'{z_score} dan {p_value}')

st.write('## CHECK NORMALITY')
clicked_2= st.button('do the shapiro test!!')

if clicked_2:
    result = shapiro(df['grades'])
    st.write(result)
    st.bar_chart(df['grades'])