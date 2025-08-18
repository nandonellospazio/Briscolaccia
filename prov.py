import streamlit as st
import pandas as pd
import utils as utils
from datetime import datetime
import constants as C

s = C.directory + "Briscolaccia_Sombreno_25.csv"
csv = pd.read_csv(s, sep=";", header=0, index_col=False)
master = pd.DataFrame(csv)
print(master)

groupby = master.groupby(['Giocatori'])

out = pd.DataFrame({'PunteggioTotale': groupby['Punteggio'].sum(),})

#master.groupby("Giocatori").groups {1: ['fox', 'gorilla'], 2: ['lion']}
#out = master.groupby(["Punteggio"]).cumsum()
master['Cumul'] = master.groupby(['Giocatori'])['Punteggio'].cumsum()

#out= master.groupby(['Giocatori']).sum().groupby(level=0).cumsum().reset_index()

#master['Cumulato'] = df['Punteggio'].cumsum()

print(master)