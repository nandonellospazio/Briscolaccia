import streamlit as st
import BackEnd as BE
import pandas as pd
from streamlit_extras.stylable_container import stylable_container
import constants as C
import utils as utils
from login_page import login
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
    player = st.selectbox('Scegli il giocatore', options=label)

    s = directory + "Briscolaccia_Sombreno_25.csv"
    csv = pd.read_csv(s, sep=";", header=0, index_col=False)
    master = pd.DataFrame(csv)
    master['Data'] = pd.to_datetime(master['Data'], format='%Y%m%d')
    out = master.loc[master['Giocatori'] == player]

    out['Cumulati'] = master.groupby(['Giocatori'])['Punteggio'].cumsum()
    # master = master.rename(columns={'Data': 'index'}).set_index('index')

    st.subheader(":rainbow[Quale è il percorso del nostro eroe?]")
    master.Progress_match: int = 0
    st.line_chart(out, x="Progress_match", y="Cumulati", x_label="Partite", y_label="Andamento punti cumulati")
    # st.bar_chart(data=out, color="#ffc1cc")

main()