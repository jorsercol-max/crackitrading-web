import streamlit as st
import streamlit.components.v1 as components
import os

# Configuració de la pàgina
st.set_page_config(page_title="CrackiTrading", layout="wide", initial_sidebar_state="collapsed")

# Inicialització de la pàgina actual
if 'pagina' not in st.session_state:
    st.session_state.pagina = "LANDING"

def carregar_html(nom_fitxer):
    base_path = os.path.dirname(__file__)
    ruta = os.path.join(base_path, "pagines", nom_fitxer)
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"<body><h1>❌ Error: No es troba {nom_fitxer}</h1></body>"

def main():
    estat = st.session_state.pagina
    
    # Mapa de navegació
    fitxers = {
        "LANDING": "landing.html",
        "LOGIN": "inici.html",
        "REGISTRE": "registre.html",
        "PAGAMENT": "pagament.html"
    }
    
    nom_arxiu = fitxers.get(estat, "landing.html")
    html_contingut = carregar_html(nom_arxiu)

    # Aquest component rep els missatges de l'HTML
    # IMPORTANT: El valor de 'res' serà el que enviem des de JS
    res = components.html(html_contingut, height=1000, scrolling=True, key=f"v_{estat}")

    # Lògica de canvi de pàgina segons el missatge rebut
    if res == "GOTO_LOGIN":
        st.session_state.pagina = "LOGIN"
        st.rerun()
    elif res == "GOTO_REGISTRE":
        st.session_state.pagina = "REGISTRE"
        st.rerun()
    elif res == "GOTO_LANDING":
        st.session_state.pagina = "LANDING"
        st.rerun()
    elif res == "GOTO_PAGAMENT":
        st.session_state.pagina = "PAGAMENT"
        st.rerun()

if __name__ == "__main__":
    main()
