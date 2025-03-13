import streamlit as st
from components.header import render_header
from components.preferences import show_preferences_form
from components.chat import show_chat_interface
from config import initialize_session_state

# Page configuration
st.set_page_config(
    page_title="Sereno AI",
    page_icon="💭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Apply custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    # Initialize session state
    initialize_session_state()

    # Render app header
    render_header()

    # Show preferences form or chat interface
    if st.session_state.user_preferences is None:
        if show_preferences_form():
            st.rerun()
    else:
        show_chat_interface()

        # Reset button (placed at the bottom right)
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col2:
                if st.button("Ricomincia", use_container_width=True):
                    st.session_state.user_preferences = None
                    st.session_state.messages = []
                    st.rerun()


if __name__ == "__main__":
    main()
