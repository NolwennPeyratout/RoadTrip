import spacy
import pandas as pd
import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from urllib.parse import quote

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD

# Create a Graph
g = Graph()

nlp = spacy.load("en_core_web_sm")
import en_core_web_sm


nlp = en_core_web_sm.load()
df = pd.DataFrame(columns=['country', 'activity'])
dfOther = pd.DataFrame(columns=['NER', 'word'])

#directory where all the paragraphs are
dossier_paragraph = os.path.join(os.getcwd(), 'paragraph')

#Word accepted or not for the activity
word_accepted=["lake", "mount", "park", "bay", "island", "crater", "valley"]
word_not_accepted=["the", "a"]

#URI of our vocabulary
countryURI = URIRef("http://example.org/country#")
activityURI = URIRef("http://example.org/activity#")

#Definition to preprocess our activities
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    # Converting to lowercase
    text = text.lower()
    # Removing punctuation
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    # Tokenization
    words = word_tokenize(text)
    # Removing stopwords and applying stemming
    #words = [ps.stem(word) for word in words if word not in stop_words]

    return ' '.join(words)

# Vérifier si le dossier existe
if os.path.exists(dossier_paragraph):
    fichiers_dans_dossier = os.listdir(dossier_paragraph)

    for fichier in fichiers_dans_dossier:
        with open("paragraph/"+fichier, 'r', encoding='utf-8') as file:
           country = fichier.split('-')[1].split('.')[0]
           for ligne in file:
               doc=nlp(ligne.strip())
               for ent in doc.ents:
                    #check if it's a location = activity and has a word in common with the list word_accepted
                    if ent.label_=="LOC" and any(word in ent.text.lower() for word in word_accepted) :
                        #remove word not accepted
                        edit_string_as_list = ent.text.lower().split()
                        final_list = [word for word in edit_string_as_list if word not in word_not_accepted]
                        activity = preprocess_text(' '.join(final_list))
                        if not ((df['country'] == country) & (df['activity'] == activity)).any():
                            #add node in the graph
                            subject = URIRef(activityURI + quote(activity))
                            hasCountry = URIRef(activityURI + "hasCountry")
                            countryObjet = URIRef(countryURI + quote(country))
                            a = RDF.type
                            classActivity = URIRef(activityURI + "RuralActivity")
                            hasActivityName = URIRef(activityURI + "hasActivityName")
                            activityName = Literal(activity)

                            g.add((subject, hasCountry, countryObjet))
                            g.add((subject, a, classActivity))
                            g.add((subject, hasActivityName, activityName))
                            #add in the dataframe
                            new_record = pd.DataFrame([{'country': country, 'activity':activity}])
                            df = pd.concat([df, new_record]).drop_duplicates(ignore_index=True)
                        

    df.to_csv('ner.csv', index=False) 

    # Affichage du graph RDF
    print("Graph RDF:")
    print(f"Graph g has {len(g)} statements.")
    with open("../ontology/NER.ttl", "w") as file:
        file.write(g.serialize(format="turtle"))
    print(g.serialize(format="turtle"))