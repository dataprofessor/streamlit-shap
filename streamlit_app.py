import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
#from streamlit_shap import st_shap
import shap

st.title('Feature importance with streamlit-shap')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
st.write(df)
