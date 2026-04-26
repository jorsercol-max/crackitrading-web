import streamlit as st
import streamlit.components.v1 as components
import os

# Configuració de la pàgina
st.set_page_config(page_title="CrackiTrading", layout="wide", initial_sidebar_state="collapsed")

# Inicialitzem l'estat de la sessió si no existeix
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'autenticat' not in st.session_state:
    st.session_state.autenticat = False

# Funció per carregar fitxers HTML
def carregar_html(fitxer):
    if os.path.exists(fitxer):
        with open(fitxer, 'r', encoding='utf-8') as f:
            return f.read()
    return f"<h1>Error: {fitxer} no trobat</h1>"

# --- LÒGICA DE NAVEGACIÓ ---

# 1. LANDING PAGE
if st.session_state.page == 'landing':
    html_landing = carregar_html('landing.html')
    # Captura el missatge del botó de la Landing
    seleccionat = components.html(html_landing, height=2000, scrolling=True)
    
    # Truc per detectar si han clicat "Accés Clients"
    # (Com que l'HTML envia un missatge, el gestionem aquí)
    st.button("Entrar al Sistema (Provisional)", on_click=lambda: st.session_state.update({"page": "login"}))

# 2. PÀGINA DE LOGIN / REGISTRE
elif st.session_state.page == 'login':
    html_login = carregar_html('inici.html') # El teu inici.html
    components.html(html_login, height=800)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Tornar a l'Inici"):
            st.session_state.page = 'landing'
            st.rerun()
    with col2:
        if st.button("Validar Accés (Demo)"):
            st.session_state.autenticat = True
            st.session_state.page = 'escriptori'
            st.rerun()

# 3. ESCRIPTORI (DASHBOARD)
elif st.session_state.page == 'escriptori':
    if not st.session_state.autenticat:
        st.session_state.page = 'login'
        st.rerun()
        
    html_escriptori = carregar_html('escriptori.html')
    components.html(html_escriptori, height=1000)
    
    if st.sidebar.button("Tancar Sessió"):
        st.session_state.autenticat = False
        st.session_state.page = 'landing'
        st.rerun()
    
    if st.sidebar.button("Configurar Alertes"):
        st.session_state.page = 'alertes'
        st.rerun()

# 4. CONFIGURACIÓ D'ALERTES
elif st.session_state.page == 'alertes':
    html_alertes = carregar_html('alertes.html')
    components.html(html_alertes, height=1000)
    
    if st.button("← Tornar a l'Escriptori"):
        st.session_state.page = 'escriptori'
        st.rerun()
