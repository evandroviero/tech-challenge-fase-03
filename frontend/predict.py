import streamlit as st
import pandas as pd
import joblib
from db_connection import get_cities
import requests


def render_prediction_page():
    model = joblib.load("model/rent_model.pkl")
    # Layout em colunas para inputs
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        city = st.selectbox("Cidade", get_cities())
        area = st.number_input("Área (m²)", min_value=10, max_value=1000, value=50)
        rooms = st.number_input("Quartos", min_value=0, max_value=10, value=2)
        bathroom = st.number_input("Banheiros", min_value=0, max_value=10, value=1)

    with col2:
        parking_spaces = st.number_input("Vagas de Estacionamento", min_value=0, max_value=10, value=1)
        floor = st.number_input("Andar", min_value=0, max_value=50, value=1)
        animal = st.selectbox("Animais Permitidos?", ["yes", "no"])
        furniture = st.selectbox("Mobiliado?", ["yes", "no"])

    with col3:
        hoa = st.number_input("Condomínio (R$)", min_value=0, max_value=10000, value=500)
        property_tax = st.number_input("IPTU (R$)", min_value=0, max_value=5000, value=200)
        fire_insurance = st.number_input("Seguro Incêndio (R$)", min_value=0, max_value=2000, value=50)

    input_data = {
        "city": city,
        "area": area,
        "rooms": rooms,
        "bathroom": bathroom,
        "parking_spaces": parking_spaces,
        "floor": floor,
        "animal": 1 if animal == "yes" else 0,
        "furniture": 1 if furniture == "yes" else 0,
        "hoa": hoa,
        "property_tax": property_tax,
        "fire_insurance": fire_insurance,
    }

    if st.button("Prever Aluguel"):
        base_url = "http://127.0.0.1:8000"
        endpoint = "/api/v1/housespredict/"

        response = requests.post(f"{base_url}{endpoint}", json=input_data)
        predicted_rent = response.json().get("predicted_rent")
        st.markdown(f"<h2 style='color: green;'>💵 Valor do aluguel previsto: R${predicted_rent}</h2>", unsafe_allow_html=True)
