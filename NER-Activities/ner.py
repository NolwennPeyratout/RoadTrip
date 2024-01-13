import spacy
import pandas as pd
import os

nlp = spacy.load("en_core_web_sm")
import en_core_web_sm


nlp = en_core_web_sm.load()
df = pd.DataFrame(columns=['country', 'activity'])
dfOther = pd.DataFrame(columns=['NER', 'word'])

dossier_paragraph = os.path.join(os.getcwd(), 'paragraph')
word_accepted=["lake", "mount", "park", "bay", "island", "crater", "valley"]
word_not_accepted=["the", "a"]



# Vérifier si le dossier existe
if os.path.exists(dossier_paragraph):
    fichiers_dans_dossier = os.listdir(dossier_paragraph)

    for fichier in fichiers_dans_dossier:
        with open("paragraph/"+fichier, 'r', encoding='utf-8') as file:
           country = fichier.split('-')[1].split('.')[0]
           for ligne in file:
               doc=nlp(ligne.strip())
               for ent in doc.ents:
                    if ent.label_=="LOC" and any(word in ent.text.lower() for word in word_accepted) :
                        edit_string_as_list = ent.text.lower().split()
                        final_list = [word for word in edit_string_as_list if word not in word_not_accepted]
                        activity = ' '.join(final_list)
                        new_record = pd.DataFrame([{'country': country, 'activity':activity}])
                        df = pd.concat([df, new_record].drop_duplicates(), ignore_index=True)
                        

    df.to_csv('ner.csv', index=False) 