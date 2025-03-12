import streamlit as st
from chat_helper import create_system_prompt, get_chat_response

# Configurazione pagina
st.set_page_config(page_title="Chat Terapeutica", page_icon="🤗", layout="wide")

# Inizializzazione stato sessione
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_preferences" not in st.session_state:
    st.session_state.user_preferences = None


def initialize_chat():
    """Initialize chat with system prompt."""
    system_prompt = create_system_prompt(st.session_state.user_preferences)
    st.session_state.messages = [{"role": "system", "content": system_prompt}]


def show_preferences_form():
    """Display and handle the preferences form."""
    with st.form("preferences_form"):
        st.write("### Qualche informazione su di te:")

        name = st.text_input("Come vuoi essere chiamato/a?")

        therapy_experience = st.selectbox(
            "Esperienza con la terapia",
            ["ha già fatto terapia", "sta valutando", "mai fatto terapia"],
        )

        objectives = st.multiselect(
            "Obiettivi personali",
            ["ridurre stress", "migliorare il sonno", "gestire emozioni"],
            default=[],
        )

        tone = st.selectbox("Preferenze di tono", ["formale", "informale"])

        style = st.selectbox("Stile di comunicazione", ["diretto", "riflessivo"])

        timing = st.multiselect(
            "Momenti della giornata in cui senti più bisogno di supporto",
            ["mattina", "sera", "momenti di ansia"],
            default=[],
        )

        submitted = st.form_submit_button("Inizia la Chat")

        if submitted:
            if not objectives:
                st.error("Seleziona almeno un obiettivo personale")
                return False
            if not timing:
                st.error("Seleziona almeno un momento della giornata")
                return False

            st.session_state.user_preferences = {
                "name": name,
                "therapy_experience": therapy_experience,
                "objectives": objectives,
                "tone": tone,
                "style": style,
                "timing": timing,
            }
            initialize_chat()
            return True
    return False


def show_chat_interface():
    """Display the chat interface."""
    st.write("### Chat Terapeutica")

    # Visualizza messaggi precedenti
    for message in st.session_state.messages[1:]:  # Skip system prompt
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar="🤗"):
                st.write(message["content"])
        else:
            with st.chat_message("user", avatar="👤"):
                st.write(message["content"])

    # Input utente
    user_input = st.chat_input("Scrivi un messaggio...")

    if user_input:
        # Aggiungi messaggio utente
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="👤"):
            st.write(user_input)

        # Ottieni e mostra risposta
        with st.chat_message("assistant", avatar="🤗"):
            with st.spinner("Sto pensando..."):
                try:
                    response = get_chat_response(st.session_state.messages)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )
                    st.write(response)
                except Exception as e:
                    st.error(f"Si è verificato un errore: {str(e)}")


def main():
    st.title("💭 Sereno AI")

    if st.session_state.user_preferences is None:
        form_submitted = show_preferences_form()
        if not form_submitted:
            return

    show_chat_interface()

    # Pulsante per ricominciare
    if st.button("Ricomincia"):
        st.session_state.user_preferences = None
        st.session_state.messages = []
        st.rerun()


if __name__ == "__main__":
    main()
