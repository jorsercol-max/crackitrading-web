import streamlit as st
import streamlit.components.v1 as components
import os

# 1. CONFIGURACIÓ DE LA PÀGINA
st.set_page_config(page_title="CrackiTrading", layout="wide", initial_sidebar_state="collapsed")

# 2. INICIALITZACIÓ DE L'ESTAT
if 'pagina' not in st.session_state:
    st.session_state.pagina = "LANDING"

# 3. FUNCIÓ PER CARREGAR HTML (Mètode robust per a Streamlit Cloud)
def carregar_html(nom_fitxer):
    # Obtenim la ruta del directori on està l'app.py
    directori_actual = os.path.dirname(os.path.abspath(__file__))
    # Ajuntem la ruta amb la carpeta 'pagines' i el fitxer
    ruta = os.path.join(directori_actual, "pagines", nom_fitxer)
    
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"<h1>Error: No s'ha trobat el fitxer {nom_fitxer} a la ruta {ruta}</h1>"

# 4. NAVEGACIÓ
def main():
    estat = st.session_state.pagina
    
    fitxers = {
        "LANDING": "landing.html",
        "LOGIN": "inici.html",
        "REGISTRE": "registre.html",
        "PAGAMENT": "pagament.html"
    }
    
    if estat in fitxers:
        contingut = carregar_html(fitxers[estat])
        
        # El retorn de dades des de l'HTML (per als botons)
        res = components.html(contingut, height=1200, scrolling=True, key=f"comp_{estat}")
        
        # Lògica de canvi de pàgina segons el que enviï el JS
        if res == "GOTO_LOGIN":
            st.session_state.pagina = "LOGIN"
            st.rerun()
        elif res == "GOTO_REGISTRE":
            st.session_state.pagina = "REGISTRE"
            st.rerun()
        elif res == "GOTO_LANDING":
            st.session_state.pagina = "LANDING"
            st.rerun()
        elif res and "LOGIN_OK" in str(res):
            st.session_state.pagina = "DASHBOARD"
            st.rerun()
            
    elif estat == "DASHBOARD":
        st.title("🚀 Panell de Control CrackiTrading")
        st.write("Benvingut a l'escriptori del bot Atheneum.")
        if st.button("Sortir"):
            st.session_state.pagina = "LANDING"
            st.rerun()

if __name__ == "__main__":
    main()
