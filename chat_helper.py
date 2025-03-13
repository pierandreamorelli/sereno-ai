from openai import OpenAI
from typing import List, Dict
import streamlit as st

MODEL = st.secrets["MODEL"]

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def create_system_prompt(user_data: Dict) -> str:
    """Create the system prompt based on user preferences."""
    base_prompt = st.secrets["SYSTEM_PROMPT"]
    return base_prompt.format(
        name=user_data.get("name", "Non specificato"),
        therapy_experience=user_data["therapy_experience"],
        objectives=", ".join(user_data["objectives"]),
        problems=", ".join(user_data["problems"]),
        tone=user_data["tone"],
        attitude=user_data["attitude"],
        initiative=user_data["initiative"],
    )


def get_chat_response(messages: List[Dict]) -> str:
    """Get response from OpenAI API."""
    try:
        response = client.chat.completions.create(
            model=MODEL, messages=messages, temperature=0.8, max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Errore nella comunicazione con OpenAI: {str(e)}")
