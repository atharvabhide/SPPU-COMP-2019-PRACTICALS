"""Shared Streamlit UI utilities for chatbot / expert-system practicals."""
import streamlit as st


def create_ask_quit_buttons():
    """Render side-by-side Ask and Quit buttons; return (ask_clicked, quit_clicked)."""
    col1, col2 = st.columns([1, 0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit_clicked = st.button("Quit")
    return ask, quit_clicked


def handle_unknown_query(knowledge_base, key):
    """Show a text input so the user can teach the knowledge base a new answer."""
    st.write(
        "Question is not present in the knowledge base!\n"
        "Could you please enter the appropriate answer for the question below-"
    )
    answer = st.text_input("Answer")
    add = st.button("Add answer")
    if add:
        knowledge_base[key] = [answer]
