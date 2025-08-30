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

# @st.cache
# def load_data(n_rows=1000):
#     time.sleep(4)  # make our function super slow
#
#     dataframe = pd.read_csv(file, nrows=n_rows)
#     return dataframe

def main():
    def click_button():
        st.session_state.clicked = True

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    st.button("Aggiorna i risultati", icon="🔥", key="button2", on_click=click_button)
    if st.session_state.clicked:
        # Lancia il backend
        BE.aggiorna()

    s = directory + "Briscolaccia_Sombreno_25.csv"
    csv = pd.read_csv(s, sep=";", header=0, index_col=False)
    master = pd.DataFrame(csv)
    master['Data'] = pd.to_datetime(master['Data'], format='%Y%m%d')

    maxPu = master['Progress_match'].max()
    st.write(":blue[Numero di partite giocate da settembre 2025: ]", maxPu)
    st.header('')

    groupby = master.groupby(['Giocatori'])
    out = pd.DataFrame({'PunteggioTotale': groupby['Punteggio'].sum(), })
    out.sort_values(by=["PunteggioTotale"], ascending=True)

    st.subheader(':rainbow[Classifica dei punti cumulati finora] :sunglasses:')
    st.bar_chart(data=out)

    groupby = master.groupby(['Giocatori'])
    out = pd.DataFrame({'TOT_Win': groupby['Winner'].sum(), })
    out.sort_values(by=["TOT_Win"], ascending=False)

    st.subheader(':green[Chi ha vinto più partite?]')
    st.bar_chart(data=out, color="#1b4d3e")

    groupby = master.groupby(['Giocatori'])
    out = pd.DataFrame({'TOT_Los': groupby['Loser'].sum(), })
    out.sort_values(by=["TOT_Los"], ascending=True)

    st.subheader(':red[Chi ha perso più partite?]')
    st.bar_chart(data=out, color=["#fe6f5e"])

    groupby = master.groupby(['Giocatori'])
    out = pd.DataFrame({'Numero partite': groupby['Giocatori'].count(), })
    out.sort_values(by=["Numero partite"], ascending=True)

    st.subheader(":blue[Chi ha giocato più partite?]")
    st.bar_chart(data=out, color="#0d98ba")

main()
