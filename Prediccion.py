import numpy as np
import streamlit as st
import pandas as pd
 
st.write(''' # Predicción del precio de la gasolina ''')
st.image("gasolina.jpg", caption="Precio de la gasolina.")
 
st.header('Datos')
st.image("Relacion de estados.png", caption="Estados.")
 
def user_input_features():
  # Entrada
  Año = st.number_input('Año (a partir de 2017):',  min_value=2017, max_value=3000, value = 2017, step = 1)
  Mes = st.number_input('Mes(ENE: 1, FEB: 2, MAR: 3, ABR: 4, MAY: 5, JUN: 6,JUL: 7,AGO: 8, SEP: 9, OCT: 10, NOV: 11, DIC: 12):', min_value=0, max_value=12, value = 0, step = 1)
  Entidad = st.number_input('Entidad (Valores del 0-32):', min_value=0, max_value=32, value = 0, step = 1)
 
 
  user_input_data = {'Año': Año,
                     'Mes': Mes,
                     'Entidad': Entidad}
 
  features = pd.DataFrame(user_input_data, index=[0])
 
  return features
 
df = user_input_features()
 
Precio =  pd.read_csv('Gasolina_1.csv', encoding='latin-1')
X = Precio.drop(columns='PRECIO')
y = Precio['PRECIO']
 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)
 
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df.Año + b1[1]*df.Mes + b1[2]*df.Entidad
 
st.subheader('Cálculo del precio')
#st.write('El precio sera', prediccion)
#st.markdown("<h2 style='text-align: center; color: #884EA0;'>Cálculo del precio</h2>", unsafe_allow_html=True)
 
st.markdown(
    f"""
<div style="text-align: center; background-color: #F2F4F4; padding: 20px; border-radius: 15px;">
<h3 style="color: #D35400;">El precio será:</h3>
<p style="font-size: 28px; font-weight: bold; color: #1F618D;">${prediccion.values[0]:.2f} MXN</p>
</div>
    """, 
    unsafe_allow_html=True
)
