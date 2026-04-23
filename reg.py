import streamlit as st
import pandas as pd
import pickle
import time

# Chargement du modele
with open('./model.pkl','rb') as file:
    model = pickle.load(file)

# Titre et mise en page
st.set_page_config(page_title="Predicteur de Charges Medicales")
st.title("Prediction de charges medicales")
st.markdown("Remplis les informations ci-dessous pour predire les charges medicales")
# Ajout d'animation
with st.spinner('Chargement du modele...'):
    time.sleep(2)

# Entrees utilsateur
col1,col2=st.columns(2)
with col1:
    age = st.slider('Age',18,100,30)
with col2:
    sex = st.selectbox('Sexe',["male","female"])
col3,col4=st.columns(2)
with col3:
    bmi = st.number_input('BMI',10.0,50.0,25.0)
with col4:
    children = st.slider('Nombre d\'enfants',0,5,1)

col5,col6=st.columns(2)
with col5:
    smoker = st.selectbox('Fumeur',["yes","no"])
with col6:
    region = st.selectbox('Region',["northeast","northwest","southeast","southwest"])

# Encodage des variables categorique
sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0
region_dict = {"southwest": 0.24308153, "southeast":0.27225131, "northwest":0.24233358, "northeast":0.27225131}
region_encoded = region_dict[region]

# Preparation des donnees pour la prediction
input_data = [(age, sex_encoded, bmi, children, smoker_encoded, region_encoded)]

# Prediction
if st.button('Predire les charges medicales'):
    with st.spinner('Predire...'):
        prediction = model.predict(input_data)[0]
        time.sleep(1)
    st.success(f'Prediction terminee!')
    st.markdown(f"### Charges medicales estimees : **{prediction:.2f} $**")
    st.balloons()