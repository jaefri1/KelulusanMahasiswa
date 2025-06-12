import streamlit as st

st.set_page_config(page_title="Dashboard Kelulusan Mahasiswa", layout="wide")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Eksplorasi Dataset", "Performa Model", "Prediksi"])

if page == "Eksplorasi Dataset":
    from pages.ekplorasi import show
    show()
elif page == "Performa Model":
    from pages.performa import show
    show()
elif page == "Prediksi":
    from pages.prediksi import show
    show()
