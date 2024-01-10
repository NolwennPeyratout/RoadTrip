import pandas as pd
import os

nom_fichier_csv = "Travel-Destinations.csv" 
dataframe = pd.read_csv(nom_fichier_csv, sep=',')

pays=dict()
pays_colonne=dataframe.iloc[:, 1].tolist()
for elem in pays_colonne:
    if pays.get(elem)==None:
        pays[elem]=1
    else:
        pays[elem]=pays[elem]+1

paysSorted = sorted(pays.items(), key=lambda x: x[1], reverse=True)

print(paysSorted)