import pandas as pd
from urllib.parse import quote

nom_fichier_csv = "Travel-Destinations.csv" 
dataframe = pd.read_csv(nom_fichier_csv, sep=',')

pays=dict()
pays_colonne=dataframe.iloc[:, 1].tolist()
with open("../ontology/countries.ttl", "w") as file:
    file.write("@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"+
"@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"+
"@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .\n"+
"@prefix owl:  <http://www.w3.org/2002/07/owl#> .\n"+
"@prefix country:  <http://example.org/country#> .\n"+
"@prefix :  <http://example.org/roadtrip#> .\n \n")
    for elem in pays_colonne:
        if pays.get(elem)==None:
            pays[elem]=1
            file.write("country:"+quote(elem)+ " a :Country; \n"
                       "    :hasCountryName \""+ elem + "\";\n"+
                       "    :hasCapital ;\n"+
                        "    :hasCurrency ;\n"+
                        "    :hasLanguage ;\n" +
                        "    :requiresVaccine .\n \n")

