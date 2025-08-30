import streamlit as st
import BackEnd as BE
import pandas as pd
import seaborn as sns
from streamlit_extras.stylable_container import stylable_container
import constants as C
import utils as utils
from login_page import login
from PIL import Image
from datetime import datetime

now = datetime.now().strftime("%Y%m%d")

label = C.label
logo = C.logo

directory = C.directory
directory_ark = C.directory_ark
path_save = directory_ark + "Partita" + now + ".csv"

exogenous_features = ['Punteggio']
predict_size = 5

cols = st.columns(len(exogenous_features))
lists = []

def main():
    # App settings
    title = "Ammazzalorso"
    # set a proper title
    image = Image.open(logo)
    st.image(image)
    st.title('La Briscolaccia dei Brenesi')
    st.subheader('Webapp per archiviare i risultati e le statistiche delle partite')
    st.header('')

    pages = {
        "Cosa puoi fare su Briscolaccia": [
            st.Page("page1.py", title="Caricare una nuova partita"),
            st.Page("page2.py", title="Vedere le statistiche generali"),
            st.Page("page3.py", title="Focus su singolo giocatore")
        ],
    }

    pg = st.navigation(pages)
    pg.run()

main()
