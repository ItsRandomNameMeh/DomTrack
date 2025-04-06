import streamlit as st
from datetime import datetime
import uuid

st.set_page_config(page_title="DomTrack — ЖКХ демо", layout="wide")
st.title("DomTrack — демо интерфейс ЖКХ-приложения")

# Инициализация хранилища заявок
if "tickets" not in st.session_state:
    st.session_state.tickets = []

# --- Блок регистрации/авторизации ---
st.sidebar.header("Пользователь")
user_type = st.sidebar.selectbox("Выберите роль", ["Жилец", "Управляющая компания"])

if user_type == "Жилец":
    st.sidebar.text_input("ФИО")
    st.sidebar.text_input("Квартира №")
else:
    st.sidebar.markdown("🔐 Роль: управляющая компания")

st.sidebar.divider()

