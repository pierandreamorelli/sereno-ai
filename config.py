import streamlit as st
from chat_helper import create_system_prompt


def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "user_preferences" not in st.session_state:
        st.session_state.user_preferences = None


def initialize_chat():
    """Initialize chat with system prompt based on user preferences"""
    system_prompt = create_system_prompt(st.session_state.user_preferences)
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
