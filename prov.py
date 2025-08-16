import streamlit as st
import pandas as pd
import utils as utils
from datetime import datetime

now = datetime.now().strftime("%Y%m%d")
directory = "/users/fernando.monaco/desktop/Varie/Briscolaccia/"
directory_ark = directory + "/Archivio/"
path_save = directory_ark + "Partita" + now + ".csv"

exogenous_features = ['Giocatore']
predict_size = 5

cols = st.columns(len(exogenous_features))
lists = []

label = ["Magio", "Re Perek", "Gazza", "Nando", "Baffo", "Carra", "Aure", "Titti", "Cina", "Dario"]

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

    for i, c in enumerate(cols):
        with c:
            for h in player:
                key = f"number_input_{i}_{h}"
                # a = st.number_input(exogenous_features[i], key=key)
                conta = st.number_input(h, min_value=-20, max_value=20, step=1, value=0,
                                        key=key)
                lists[i].append(conta)

            z = list(player)
            lists.index(z)
            d = "giocatore"
            e = "punteggio"

            if conta > 10:
                st.text("Che punteggi roboanti. Sei sicuro del punteggio?")
            elif conta < -10:
                verifica = "Che disastro per", i, ". Sei sicuro del punteggio?"
                st.text(verifica)
            j = j + 1
            somma = somma + conta

df = pd.DataFrame(lists)
df = df.transpose()
df.columns = exogenous_features
a = st.write(df)
print(a)
utils.save_partita(df, path_save)
