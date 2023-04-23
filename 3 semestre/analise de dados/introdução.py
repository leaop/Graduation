import requests
import pandas as pd
import json
import seaborn

#Dados abertos das despesas dos senadores
response = requests.get('https://adm.senado.gov.br/adm-dadosabertos/api/v1/senadores/despesas_ceaps/2018/').content
#Analise do que foi pego
data = json.loads(response)
#normalização da data bagunçacada
df = pd.json_normalize(data)
# Realizar consumo dos dados via api de forma automatizada de 2015 à 2022.

datas = [2015,2016,2017,2018,2019,2020,2021,2022]
#para uma variável em data: response é iagual ao request
#se o X variavel for igual as datas (a minima), a 'data' vai receber o arquivo já convertido
#caso contrário, ele vai adicionar a proxima ao primeiro arquivo convertido

for x in datas:
    response = requests.get('https://adm.senado.gov.br/adm-dadosabertos/api/v1/senadores/despesas_ceaps/{}/'.format(x)).content

    if x == min(datas):
        data = json.loads(response)
    else:
        data.extend(json.loads(response))
        
df = pd.json_normalize(data)

#conversao para CSV
df.to_csv('ceaps_senado_2015_2022.csv')

#dados de legislatura
response = requests.get('https://legis.senado.leg.br/dadosabertos/senador/lista/legislatura/55/56.json').content

data = json.loads(response)

data['ListaParlamentarLegislatura']['Parlamentares']['Parlamentar'];

df_senadores = pd.json_normalize(data)

df_senadores.to_csv('senadores_2015_2022.csv')
df_senadores = pd.read_csv('senadores_2015_2022.csv')
df = pd.read_csv('ceaps_senado_2015_2022.csv')
df.ano.min()


