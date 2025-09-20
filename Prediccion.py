import numpy as np
import streamlit as st
import pandas as pd
 
st.set_page_config(page_title="Predicción Gasolina", page_icon="⛽", layout="centered")
 
st.title("⛽ Predicción del precio de la gasolina Regular ⛽")
st.image("gasolina.jpg", caption="gasolina regular.")
 
#Datos de referencia
st.header("Datos de referencia")
st.image("Relacion de estados.png", caption="Estados de México")
 
st.header("📊 Ingrese los datos para la predicción")
 
def user_input_features():
  # Entrada
  Año = st.slider('Año',  min_value=2017, max_value=3000, value = 2024, step = 1)
  Meses = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
  }
 
  mes_nombre = st.selectbox("Mes", list(Meses.keys()))
  Mes = Meses[mes_nombre]

  Entidades = {
      "Nacional": 17,	"Aguascalientes": 0,	"Baja California": 1,	"Baja California Sur": 2, "Campeche": 3,	"Chiapas": 4,	"Chihuahua": 5,
      "Ciudad de México": 6,	"Coahuila de Zaragoza": 7,	"Colima": 8,	"Durango": 9,	"Guanajuato": 10,	"Guerrero": 11,	"Hidalgo": 12,
      "Jalisco": 13,	"Michoacán de Ocampo": 14,	"Morelos": 15,	"México": 16,	"Nayarit": 18,	"Nuevo León": 19, "Oaxaca": 20,	"Puebla": 21,
      "Querétaro": 22,	"Quintana Roo": 23,	"San Luis Potosí": 24,	"Sinaloa":25,	"Sonora": 26,	"Tabasco": 27,	"Tamaulipas": 28,	"Tlaxcala": 29,
      "Veracruz": 30,	"Yucatán": 31,	"Zacatecas": 32
      }
  entidad_nombre = st.selectbox("Entidad", list(Entidades.keys()))
  Entidad = Entidades[entidad_nombre]
 
 
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
 
st.subheader("💡 Resultado de la predicción")
st.markdown(
    f"""
<div style="text-align: center; background-color: #F2F4F4; padding: 20px; border-radius: 15px;">
<h3 style="color: #D35400;">El precio será:</h3>
<p style="font-size: 28px; font-weight: bold; color: #1F618D;">${prediccion.values[0]:.2f} MXN</p>
</div>
    """,
    unsafe_allow_html=True
)
