import streamlit as st
import BackEnd as BE
import constants as C
import pandas as pd
import utils as utils
from streamlit_extras.stylable_container import stylable_container
from datetime import datetime

now = datetime.now().strftime("%Y%m%d")

label = C.label
label = ["Magio", "Re Perek", "Gazza", "Nando", "Baffo", "Carra", "Aure", "Titti", "Cina", "Dario"]

directory = "/users/fernando.monaco/desktop/Varie/Briscolaccia/"
directory_ark = directory + "/Archivio/"
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
    # App settings
    title = "Ammazzalorso"
    # set a proper title
    st.header('La Briscolaccia dei Brenesi')
    st.header('Webapp per archiviare risultati delle partite e mantenere uno storico')
    st.header('')
    tab1, tab2, tab3 = st.tabs(["Carica Risultato", "📈 Storico", "Analisi giocatori"])
    contaz = 0

    with tab1:
        player= st.multiselect('Inserisci i giocatori dalla seguente lista', options=label)
        contaz = len(player)
        if contaz > 5:
            st.text("Ci sono troppi giocatori, ricontrolla")
        elif contaz < 5:
            delta = 5-contaz
            testo = "Aggiungi altri", delta, "giocatori"
            st.text(testo)
        else:
            st.write("I giocatori sono: ", player)

            #Caricare i punteggio giocatore per giocatore
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


                #d=(d, i)
                #e=(e, conta)
                #partita = partita.insert(-1,str(player))
                #partita = partita.insert(-1, conta)
                #data2 = {"giocatore": [player], "punteggio": [conta], "data": [now]}
                #data2 = pd.DataFrame(data2)
                #nuova_partita = nuova_partita.append(data2)
            if somma != 0:
                st.text("C'è qualcosa che non va nella somma dei punteggi")
                #print(partita, player)
            else:
                # Create buttons with st.button
                #print(partita, player, conta)
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
                        #df.set_index(list(player))
                        df.insert(0, "Giocatori",player)
                        df.insert(0, "Data", now)
                        utils.save_partita(df, path_save)
                        st.write('Partita caricata!')

    # for i in label:
    #     st.checkbox(i, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False,
    #             label_visibility="visible", width="content")
    #     if check_boxes:
    #         st.write(i)
    # if question != "":
    #     risposta = be_app.gpt3(question)
    #     st.write(risposta[0])
    #     now = datetime.now().strftime("%Y%m%d %H:%M:%S")
    #     utils.salva_q(question, risposta[1], risposta[2], now)

    #utils.add_bg_from_local(directory+"Area591_logo.png")

main()

# #  define our sidebar title
# st.sidebar.title("Menu")
# #  define our sidebar subtitle
# st.sidebar.subheader("Select feature")
#
# max_rows = st.slider(
#     "Number of observation to show",
#     min_value=2000,
#     max_value=47660,  # should be set automatically
#     value=2000,
#     step=1000,
# )
#
# # our dataset
# df = load_data(max_rows)
#
# # show to the user how many records are loaded
# st.write("Records shown: ", df.shape[0])
#
# # get a list of all numeric columns
# numeric_columns = df.select_dtypes(exclude=object).columns.values
#
# # create a feature picker
# feature = st.sidebar.selectbox(
#     "Click below to select a new feature",
#     numeric_columns
# )
#
# # Canvas
# sns.distplot(df[feature])
# st.pyplot()
