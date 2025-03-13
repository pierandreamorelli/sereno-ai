import streamlit as st
from chat_helper import get_chat_response


def show_chat_interface():
    """Display the chat interface"""
    # Welcome message
    if len(st.session_state.messages) == 1:  # Only system prompt exists
        name = st.session_state.user_preferences.get("name", "")
        greeting = f"Ciao {name}! " if name else "Ciao! "
        welcome_msg = (
            f"{greeting}Sono qui per parlare con te. Come posso aiutarti oggi?"
        )

        # Add assistant's welcome message
        st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

    # Chat container for styling
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    st.markdown("<h3>Chat</h3>", unsafe_allow_html=True)

    # Display chat messages
    for message in st.session_state.messages[1:]:  # Skip system prompt
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar="🤗"):
                st.write(message["content"])
        else:
            with st.chat_message("user", avatar="👤"):
                st.write(message["content"])

    # User input
    user_input = st.chat_input("Scrivi un messaggio...")

    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display user message
        with st.chat_message("user", avatar="👤"):
            st.write(user_input)

        # Get and display assistant response
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

    st.markdown("</div>", unsafe_allow_html=True)
