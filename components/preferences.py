import streamlit as st
from config import initialize_chat


def show_preferences_form():
    """Display and handle the user preferences form"""
    # st.markdown("<div class='form-container'>", unsafe_allow_html=True)

    st.markdown("### Qualche informazione su di te")

    with st.form("preferences_form", clear_on_submit=False):
        # Form fields
        name = st.text_input("Come vuoi essere chiamato/a?")

        # st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        therapy_experience = st.selectbox(
            "Hai mai fatto terapia?",
            [
                "Si, in passato",
                "Si, sono in terapia su Serenis (o altro)",
                "No, sto valutando questa possiblità",
                "No, non è una cosa che mi interessa, voglio solo parlare",
            ],
            index=None,
        )
        # st.markdown("</div>", unsafe_allow_html=True)

        # st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        objectives = st.multiselect(
            "Perché sei qui?",
            [
                "Provo spesso stati d'ansia",
                "Mi sento triste e giù di morale",
                "Ho difficoltà con mio figlio/mia figlia",
                "Voglio crescere come persona",
                "Ho difficoltà con la mia relazione",
                "Voglio esplorare la mia identità di genere",
                "Si tratta della sfera sessuale",
                "È successa una cosa che mi ha cambiato",
                "Sto avendo problemi col lavoro",
                "Penso di avere un problema con il cibo",
                "Altro",
            ],
            default=[],
        )
        # st.markdown("</div>", unsafe_allow_html=True)

        # st.markdown("<div class='form-section'>", unsafe_allow_html=True)
        problems = st.multiselect(
            "Ti riconosci in qualcuna di queste risposte?",
            [
                "Vorrei superare una paura specifica (volare, guidare...)",
                "Mi capita di sentire voci che nessuno sente, o di vedere cose che nessuno vede",
                "Penso di avere una dipendenza (alcol, gioco, stupefacenti...)",
                "Metto in atto dei comportamenti ripetitivi (lavo le mani molto spesso, compio dei riti...)",
                "Ho una condizione fisica che peggiora la mia qualità di vita",
                "Mi è successo di farmi del male apposta (tagli, bruciature...)",
                "Nessuna di queste",
            ],
            default=[],
        )
        # st.markdown("</div>", unsafe_allow_html=True)

        # Preferences in columns for better layout
        col1, col2 = st.columns(2)

        with col1:
            tone = st.selectbox(
                "Preferenze di tono", ["Formale", "Informale"], index=None
            )

        with col2:
            attitude = st.selectbox(
                "Tipo di atteggiamento",
                ["Razionale e pragmatico", "Riflessivo e meditativo"],
                index=None,
            )

        initiative = st.selectbox(
            "Dovrebbe guidare la conversazione o lasciarti l'iniziativa?",
            ["Guidare la conversazione", "Lasciarmi l'iniziativa", "Indifferente"],
            index=None,
        )

        # Submit button with custom styling
        submitted = st.form_submit_button("Inizia la Chat", use_container_width=True)

        if submitted:
            if not therapy_experience:
                st.error("Per favore, completa il campo 'Hai mai fatto terapia?'")
                return False
            elif not objectives:
                st.error("Per favore, completa il campo 'Perché sei qui?'")
                return False
            elif not problems:
                st.error(
                    "Per favore, completa il campo 'Ti riconosci in qualcuna di queste risposte?'"
                )
                return False
            elif not tone:
                st.error("Per favore, completa il campo 'Preferenze di tono'")
                return False
            elif not attitude:
                st.error("Per favore, completa il campo 'Tipo di atteggiamento'")
                return False
            elif not initiative:
                st.error(
                    "Per favore, completa il campo 'Dovrebbe guidare la conversazione o lasciarti l'iniziativa?'"
                )
                return False

            # Save preferences
            st.session_state.user_preferences = {
                "name": name,
                "therapy_experience": therapy_experience,
                "objectives": objectives,
                "problems": problems,
                "tone": tone,
                "attitude": attitude,
                "initiative": initiative,
            }

            # Initialize chat with system prompt
            initialize_chat()
            return True

    # st.markdown("</div>", unsafe_allow_html=True)
    return False
