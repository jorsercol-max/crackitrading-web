import streamlit as st
import streamlit.components.v1 as components
import os

# Configura la pàgina
st.set_page_config(page_title="CrackiTrading", layout="wide")

# Inicialitza l'estat
if 'pagina' not in st.session_state:
    st.session_state.pagina = "LANDING"

def carregar_html(nom_fitxer):
    # Ruta absoluta per a Streamlit Cloud
    directori_actual = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(directori_actual, "pagines", nom_fitxer)
    
    if not os.path.exists(ruta):
        return f"<h1>⚠️ Error: No s'ha trobat el fitxer {nom_fitxer}</h1><p>Ruta: {ruta}</p>"
    
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"<h1>⚠️ Error llegint {nom_fitxer}</h1><p>{str(e)}</p>"

def main():
    estat = st.session_state.pagina
    
    fitxers = {
        "LANDING": "landing.html",
        "LOGIN": "inici.html",
        "REGISTRE": "registre.html",
        "PAGAMENT": "pagament.html"
    }
    
    # Agafem el nom del fitxer o landing per defecte
    nom_arxiu = fitxers.get(estat, "landing.html")
    contingut = carregar_html(nom_arxiu)

    # SEGURETAT: Si 'contingut' no és una cadena de text, Streamlit peta.
    # Ens assegurem que sempre sigui text.
    if contingut:
        res = components.html(str(contingut), height=1200, scrolling=True, key=f"c_{estat}")
        
        # Lògica de navegació
        if res == "GOTO_LOGIN":
            st.session_state.pagina = "LOGIN"
            st.rerun()
        elif res == "GOTO_REGISTRE":
            st.session_state.pagina = "REGISTRE"
            st.rerun()
        elif res == "GOTO_LANDING":
            st.session_state.pagina = "LANDING"
            st.rerun()
    else:
        st.error(f"No s'ha pogut carregar cap contingut per a: {estat}")

if __name__ == "__main__":
    main()
