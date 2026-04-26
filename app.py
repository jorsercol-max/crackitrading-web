import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="CrackiTrading", layout="wide")

if 'pagina' not in st.session_state:
    st.session_state.pagina = "LANDING"

def carregar_html(nom_fitxer):
    # Intentem trobar la ruta de forma manual i neta
    base_path = os.path.dirname(__file__)
    ruta = os.path.join(base_path, "pagines", nom_fitxer)
    
    if not os.path.exists(ruta):
        return f"<body><h1>❌ Fitxer no trobat</h1><p>No trobo {nom_fitxer} a {ruta}</p></body>"
    
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            contingut = f.read()
            if not contingut.strip():
                return "<body><h1>⚠️ Fitxer buit</h1></body>"
            return contingut
    except Exception as e:
        return f"<body><h1>❌ Error de lectura</h1><p>{str(e)}</p></body>"

def main():
    # Diccionari de pàgines
    fitxers = {
        "LANDING": "landing.html",
        "LOGIN": "inici.html",
        "REGISTRE": "registre.html",
        "PAGAMENT": "pagament.html"
    }
    
    nom_arxiu = fitxers.get(st.session_state.pagina, "landing.html")
    html_final = carregar_html(nom_arxiu)

    # El TypeError sol venir d'aquí. Forcem que sigui STRING.
    try:
        components.html(str(html_final), height=1000, scrolling=True)
    except Exception as e:
        st.error(f"Error crític de Streamlit: {e}")
        st.code(html_final[:500]) # Mostrem els primers 500 caràcters per veure què hi ha

if __name__ == "__main__":
    main()
