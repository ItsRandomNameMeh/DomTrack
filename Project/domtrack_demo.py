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
    st.sidebar.markdown("Роль: управляющая компания")

st.sidebar.divider()
# --- Подача заявки ---
if user_type == "Жилец":
    st.header("Подать заявку")

    with st.form("ticket_form"):
        title = st.text_input("Тема заявки")
        description = st.text_area("Описание проблемы")
        category = st.selectbox("Тип проблемы", ["Протечка", "Свет", "Отопление", "Другое"])
        submitted = st.form_submit_button("Отправить заявку")

        if submitted:
            new_ticket = {
                "id": str(uuid.uuid4())[:8],
                "title": title,
                "description": description,
                "category": category,
                "status": "Ожидает",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            st.session_state.tickets.append(new_ticket)
            st.success("Заявка отправлена!")

# --- Просмотр всех заявок ---
st.header("Все заявки")
if not st.session_state.tickets:
    st.info("Заявок пока нет.")
else:
    for ticket in st.session_state.tickets:
        with st.expander(f"{ticket['id']} | {ticket['title']} [{ticket['status']}]"):
            st.write("**Тип:**", ticket["category"])
            st.write("**Описание:**", ticket["description"])
            st.write("**Создана:**", ticket["created_at"])

            # Обновление статуса — только для УК
            if user_type == "Управляющая компания":
                new_status = st.selectbox(
                    f"Изменить статус заявки {ticket['id']}",
                    ["Ожидает", "В работе", "Выполнено"],
                    index=["Ожидает", "В работе", "Выполнено"].index(ticket["status"]),
                    key=f"status_{ticket['id']}"
                )
                if new_status != ticket["status"]:
                    ticket["status"] = new_status
                    st.success(f"Статус обновлён до: {new_status}")


