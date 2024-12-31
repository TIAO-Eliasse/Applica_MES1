import streamlit as st
import pandas as pd




st.markdown("""
<style>
/* Ajuste la largeur totale du conteneur principal */
[data-testid="stAppViewContainer"] {
    max-width: 100%; /* Ajustez la largeur à 95% de l'écran */
    padding-left: 0rem; /* Supprime les marges latérales */
    padding-right: 0rem;
    margin-left: auto;
    margin-right: auto;
}

/* Réduit les marges des blocs pour un meilleur alignement */
[data-testid="block-container"] {
    padding: 1rem 0rem; /* Ajoute un espacement en haut et en bas uniquement */
}

/* Permet d'afficher plusieurs graphiques sur une même ligne */
[data-testid="stHorizontalBlock"] > div {
    flex: 1; /* Répartit l'espace horizontalement */
    margin-right: 1rem; /* Ajoute un espace entre les colonnes */
}

/* Améliore la gestion des composants interactifs */
[data-testid="stSidebar"] {
    padding-left: 0rem;
    padding-right: 0rem;
}
</style>
""", unsafe_allow_html=True)

st.write("Mecanisme de transmission des fluctuations des prix de pétrole dans l'économmie de la Guinée Equatoriale")







data=pd.read_excel("C:\Users\elias\Desktop\Application_MES\base_final.xlsx")
st.head(data)
Var=['Années', 'INV($US)', 'RECT', ' DEPT', 'TPIB', 'INF', 'CHO', 'EPG',
       'BLE', 'PRP', 'LPRP', 'MM(%)', 'MM(FCFA)', 'EXP', 'IMP', 'Tchange',
       'CDI($US)', 'Subv', 'TPOA', 'TPOA(%)', 'LIPC', 'IPC', 'Taxe',
       'Ttaxe(%)', 'TCDI(%)', 'TINV(%)', 'TEXP(%)', 'TIMP(%)']

var_réel=["TPIB","CHO",'TINV(%)','TPOA']
var_xterieur=['TEXP(%)','TIMP(%)']

var_finance=['MM(%)','TCDI(%)''INF']
var_budget=['RECT', ' DEPT','Ttaxe(%)']


