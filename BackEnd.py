import constants as C
import pandas as pd
import os
import utils as utils
from datetime import datetime

now = datetime.now().strftime("%Y%m%d")
label = C.label

def aggiorna():

    directory = C.directory
    directory_ark = C.directory_ark

    start = directory + "Briscolaccia_Sombreno_25_skeleton.csv"
    s = directory + "Briscolaccia_Sombreno_25.csv"
    csv = pd.read_csv(start, sep=";", header=0, index_col=False)
    master = pd.DataFrame(csv)

    num_partite: int = 0
    # Cicla per tutte le cartelle in input
    os.chdir(directory_ark)
    try:
        os.remove(".ds_store")
    except:
        pass
    for folder in os.walk(directory_ark):
        directory = folder[0]
        directory_name = directory.split('/')[-1]
        directory = directory + "/"
        directory = directory.replace('//', '/')
        # Cicla per ciascun file in input
        for file in folder[2]:
            f = directory + file
            partita = pd.read_csv(f, sep=",", header=0, index_col=False)
            num_partite = num_partite + 1
            maxPu = partita['Punteggio'].max()
            minPu = partita['Punteggio'].min()
            partita["MaxPunteggio"] = maxPu
            partita["MinPunteggio"] = minPu
            partita["Progress_match"] = num_partite
            partita["Winner"] = None
            partita["Loser"] = None
            for i in range(len(partita)):
                da = partita["Punteggio"][i]
                if da == maxPu:
                    partita["Winner"][i] = 1
                if da == minPu:
                    partita["Loser"][i] = 1
            master = master._append(partita)
        master.sort_values("Data")
        master.to_csv(s, sep=';', na_rep='', float_format=int, header=True, index=False, index_label=None,)

