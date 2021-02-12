import pandas as pd
import pathlib
from IPython.display import display
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split

if __name__ == '__main__':

    meses = {
        "jan": 1,
        "fev": 2,
        "mar": 3,
        "abr": 4,
        "mai": 5,
        "jun": 6,
        "jul": 7,
        "ago": 8,
        "set": 9,
        "out": 10,
        "nov": 11,
        "dez": 12,
    }
    # criamos um dicionario dos meses

    caminho_bases = pathlib.Path("dataset")
    # criamos uma variavel que recebe o caminho base usado, facilitando no momento de lidar com os arquivos de uma pasta

    base_airbnb = pd.DataFrame()
    # criamos uma tabela

    for arquivo in caminho_bases.iterdir():
        nome_mes = arquivo.name[:3]
        # os tres primeiros caracteres de cada arquivo se refere a um mes

        mes = meses[nome_mes]
        # transformamos esse mes em numero

        if mes == 2:
            break

        ano = arquivo.name[-8:]
        # os ultimos 8 caracteres contem o ano
        ano = int(ano.replace(".csv", ""))
        # mas nao queremos pegar a extensão do arquivo

        df = pd.read_csv(caminho_bases / arquivo.name, low_memory=False)
        # lemos o arquivo da pasta dataset

        df["ano"] = ano
        df["mes"] = mes
        # adicionamos as colunas mes e ano

        base_airbnb = base_airbnb.append(df)
        # adicionamos df ao nosso data frame principal

    display(base_airbnb)

colunas = ['host_response_time', 'host_response_rate', 'host_is_superhost', 'host_listings_count', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 'amenities', 'price', 'security_deposit', 'cleaning_fee', 'guests_included', 'extra_people', 'minimum_nights', 'maximum_nights', 'number_of_reviews', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value', 'instant_bookable', 'is_business_travel_ready', 'cancellation_policy', 'ano', 'mes']
# definimos as colunas que são necessárias

base_airbnb = base_airbnb.loc[:, colunas]
# criamos um "novo" dataframe, apenas com essas colunas

print(list(base_airbnb.columns))
display(base_airbnb)

