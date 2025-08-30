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
    if login():
        player = st.multiselect('Inserisci i giocatori dalla seguente lista', options=label)
        contaz = len(player)
        if contaz > 5:
            st.text("Ci sono troppi giocatori, ricontrolla")
        elif contaz < 5:
            delta = 5 - contaz
            testo = "Aggiungi altri", delta, "giocatori"
            st.text(testo)
        else:
            st.write("I giocatori sono: ", player)

            # Caricare i punteggio giocatore per giocatore
            st.text("Inserisci il punteggio finale per ciascun giocatore")
            somma = 0
            j = 0

            for p in range(len(exogenous_features)):
                lists.append([])

            for i in enumerate(cols):
                for h in player:
                    key = f"number_input_{i}_{h}"
                    # a = st.number_input(exogenous_features[i], key=key)
                    conta = st.number_input(h, min_value=-20, max_value=20, step=1, value=0,
                                            key=key)
                    lists[0].append(conta)

                    # z = list(player)
                    # lists.index(z)
                    # d = "giocatore"
                    # e = "punteggio"

                    if conta > 10:
                        st.text("Che punteggi roboanti. Sei sicuro del punteggio?")
                    elif conta < -10:
                        verifica = "Che disastro per", i, ". Sei sicuro del punteggio?"
                        st.text(verifica)
                    j = j + 1
                    somma = somma + conta

                # d=(d, i)
                # e=(e, conta)
                # partita = partita.insert(-1,str(player))
                # partita = partita.insert(-1, conta)
                # data2 = {"giocatore": [player], "punteggio": [conta], "data": [now]}
                # data2 = pd.DataFrame(data2)
                # nuova_partita = nuova_partita.append(data2)
            if somma != 0:
                st.text("C'è qualcosa che non va nella somma dei punteggi")
                # print(partita, player)
            else:
                # Create buttons with st.button
                with stylable_container(
                        "green",
                        css_styles="""
                    button {
                        background-color: #00FF00;
                        color: black;
                    }""",
                ):
                    if 'clicked' not in st.session_state:
                        st.session_state.clicked = False


                    def click_button():
                        st.session_state.clicked = True


                    carica = st.button("Salva il risultato", icon="🔥", key="button1", on_click=click_button)

                    if st.session_state.clicked:
                        # The message and nested widget will remain on the page
                        df = pd.DataFrame(lists)
                        df = df.transpose()
                        df.columns = exogenous_features
                        # df.set_index(list(player))
                        df.insert(0, "Giocatori", player)
                        df.insert(0, "Data", now)
                        utils.save_partita(df, path_save)
                        st.write('Partita caricata!')

main()