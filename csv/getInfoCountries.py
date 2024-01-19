import pandas as pd
from urllib.parse import quote

nom_fichier_csv = "Travel-Destinations.csv" 
csvFileInfos = "countries.csv" 
dataframe = pd.read_csv(nom_fichier_csv, sep=',')
dataframeInfo = pd.read_csv(csvFileInfos, sep=',')

merged_df = pd.merge(dataframe, dataframeInfo, left_on='Location', right_on='name')

merged_df = merged_df.drop(['Name','name', 'id', 'Image','iso3', 'iso2', 'currency_symbol', "tld", "native", "subregion", "latitude", "longitude", "emoji", "emojiU"], axis=1)

merged_df = merged_df.drop_duplicates()

merged_df['Location'] = merged_df['Location'].apply(lambda x: quote(str(x).encode('utf-8')))

merged_df['capital'] = merged_df['capital'].apply(lambda x: quote(str(x).encode('utf-8')))


merged_df.to_csv('../Data-Lifting/csvw/countries/countries.csv',index =False, sep=',')