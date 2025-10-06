import streamlit as st
from predict import render_prediction_page
from frontend.analysis import plot_graphical

st.set_page_config(page_title="Previsão de Aluguel", layout="wide")


st.sidebar.title("Menu")
pagina = st.sidebar.radio("Navegação", ["🏠 Home", "📈 Análises", "🔮 Predição"])

def get_text():
    text = """ Bem-vindo ao **Sistema de Predição de Preço de Imóveis**!
    Este sistema foi desenvolvido para:
    - Permitir a análise de dados de imóveis.
    - Visualizar gráficos categóricos e estatísticos.
    - Realizar **predições de preços** com base em características dos imóveis.

    Navegue pelas páginas usando o menu para explorar:
    1. **Home** – Esta página inicial.
    2. **Análise** – Visualização de dados e gráficos.
    3. **Predição** – Estime o valor de um imóvel fornecendo suas características.
    """
    return text

cat_cols = ["city", "rooms", "bathroom", "parking_spaces", "floor", "animal", "furniture"]
if pagina == "🏠 Home":
    st.markdown(get_text())
elif pagina == "📈 Análises":
    st.write("Selecione a infomação que deseja visualizar:")
    selected_col = st.selectbox("", cat_cols)
    plot_graphical(selected_col)
elif pagina == "🔮 Predição":
    st.title("💰 Previsão do Valor do Aluguel")
    st.write("Preencha os dados do imóvel abaixo e clique em **Prever Aluguel**:")
    render_prediction_page()
