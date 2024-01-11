import spacy
import pandas as pd
import os

nlp = spacy.load("en_core_web_sm")
import en_core_web_sm


nlp = en_core_web_sm.load()
df = pd.DataFrame(columns=['country', 'activity'])
dfOther = pd.DataFrame(columns=['NER', 'word'])

dossier_paragraph = os.path.join(os.getcwd(), 'paragraph')

# Vérifier si le dossier existe
if os.path.exists(dossier_paragraph):
    fichiers_dans_dossier = os.listdir(dossier_paragraph)

    for fichier in fichiers_dans_dossier:
        with open("paragraph/"+fichier, 'r', encoding='utf-8') as file:
           country = fichier.split('-')[1].split('.')[0]
           for ligne in file:
               doc=nlp(ligne.strip())
               for ent in doc.ents:
                    if ent.label_=="LOC":
                        nouvelle_ligne = {'country': country, 'activity': ent.text}
                        df = df.append(nouvelle_ligne, ignore_index=True)
                        print(ent.text, ent.label_)
                    else:
                        nouvelle_ligne = {'NER': ent.label_, 'word': ent.text}
                        dfOther = dfOther.append(nouvelle_ligne, ignore_index=True)
                        
    # fichier1="paragraph/"+fichiers_dans_dossier[0]
    # with open(fichier1, 'r', encoding='utf-8') as file:
    #        country = fichier1.split('-')[1].split('.')[0]
    #        for ligne in file:
    #            doc=nlp(ligne.strip())
    #            for ent in doc.ents:
    #                 if ent.label_=="LOC":
    #                     nouvelle_ligne = {'pays': country, 'activity': ent.text}
    #                     df = df.append(nouvelle_ligne, ignore_index=True)
    #                     print(ent.text, ent.label_)
                    
    #print(df)
    #print(dfOther)