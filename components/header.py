import streamlit as st


def render_header():
    """Render app header with logo and title"""
    st.markdown(
        "<div class='header'><span class='logo'>💭</span> Sereno AI</div>",
        unsafe_allow_html=True,
    )

    # Subtle divider
    st.markdown("<hr class='header-divider'>", unsafe_allow_html=True)
