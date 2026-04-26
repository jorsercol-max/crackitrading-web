import streamlit as st
import streamlit.components.v1 as components
import os

# Configuració de la pàgina
st.set_page_config(page_title="CrackiTrading | Bot de Trading", layout="wide", initial_sidebar_state="collapsed")

# Estats de navegació: 'landing', 'login', 'dashboard'
if 'estat' not in st.session_state:
    st.session_state.estat = 'landing'
if 'autenticat' not in st.session_state:
    st.session_state.autenticat = False

# Neteja de la interfície de Streamlit per centrar-nos en els teus HTML
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container { padding: 0rem; }
        iframe { border: none !important; }
    </style>
""", unsafe_allow_html=True)

def carregar_html(nom_fitxer, altura=1000):
    if os.path.exists(nom_fitxer):
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            return components.html(f.read(), height=altura, scrolling=True)
    return st.error(f"No s'ha trobat el fitxer {nom_fitxer} a la carpeta.")

# --- LÒGICA DE NAVEGACIÓ ---

# 1. LANDING PAGE
if st.session_state.estat == 'landing':
    # La landing és llarga, li donem força altura
    res = carregar_html("landing.html", altura=4500)
    
    # Nota: El botó d'accés de la landing hauria d'enviar el missatge 'GOTO_LOGIN'
    if res == "GOTO_LOGIN":
        st.session_state.estat = 'login'
        st.rerun()

# 2. PANTALLA DE LOGIN
elif st.session_state.estat == 'login':
    res_login = carregar_html("inici.html", altura=900)
    
    if res_login:
        if res_login == "GOTO_LANDING":
            st.session_state.estat = 'landing'
            st.rerun()
        else:
            dades = str(res_login).split("|")
            if len(dades) == 2:
                email, psw = dades
                # Les teves credencials de soci
                if email.strip() == "jorsercol@gmail.com" and psw.strip() == "papilaia7792":
                    st.session_state.autenticat = True
                    st.session_state.estat = 'dashboard'
                    st.rerun()
                else:
                    st.sidebar.error("❌ Credencials incorrectes")

# 3. DASHBOARD ATHENEUM (L'escriptori privat)
elif st.session_state.estat == 'dashboard':
    if st.session_state.autenticat:
        carregar_html("escriptori.html", altura=2000)
        
        # Botó discret de Streamlit per sortir si cal
        with st.sidebar:
            if st.button("🚪 Tancar Sessió"):
                st.session_state.autenticat = False
                st.session_state.estat = 'landing'
                st.rerun()
    else:
        st.session_state.estat = 'login'
        st.rerun()
