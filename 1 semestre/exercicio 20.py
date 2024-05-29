import urllib.request
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
URL = 'https://dados.anvisa.gov.br/dados/TA_PRECO_MEDICAMENTO.csv'
Data = pd.read_csv(URL, encoding='latin1', sep=';', low_memory=False)
Data.shape
Data.head()
df = urllib.request.urlopen(URL)
for row in df:
    print(row)
    break