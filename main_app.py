import streamlit as st
import pandas as pd
import numpy as np
import pickle

file1 = open('model.pkl', 'rb')
rf = pickle.load(file1)
file1.close()

st.title('Body fat estimator')

Density = st.number_input('Your density')

Abdomen = st.number_input('Size of your Abdomen')

Chest = st.number_input('Size of your Chest')

Weight = st.number_input('Size of your Weight')

Hip= st.number_input('Size of your hip')

Thigh = st.number_input('Size of your thigh')

Knee = st.number_input('Size of your knee')

if st.button('Predict'):

    
    input_df = pd.DataFrame({'Density': [Density], 'Abdomen': [Abdomen], 'Chest': [Chest], 'Hip': [Hip], 'Weight': [
                            Weight], 'Thigh': [Thigh], 'Knee': [Knee]})
    st.write(input_df)

    prediction = round(rf.predict(input_df)[0],2)

    st.title("Predicted Body fat for you could be between " +
             str(prediction-0.6)+ " to " + str(prediction+0.6))
