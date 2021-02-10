import pandas as pd
import plotly.express as px
from IPython.display import display


def gera_grafico_coluna(coluna, tabela):
    fig = px.histogram(tabela, x=coluna, color="Categoria")
    # geramos um grafico de histograma, em que o eixo x é definido pela coluna passada
    # e as cores são baseadas na quantidade de cada categoria, que corresponde aquela coluna

    fig.show()
    # mostramos a figura


if __name__ == '__main__':

    clients_df = pd.read_csv("ClientesBanco.csv", encoding="latin1")
    # recebemos os dados de uma tabela do tipo csv, que contém caracteres latinos

    clients_df = clients_df.drop("CLIENTNUM", axis=1)
    # apagamos uma coluna, chamada CLIENTNUM
    # a base original não é afetada

    clients_df = clients_df.dropna()
    # nós apagamos todas as linhas que possuem alguma célula vazia

    desc_clients = clients_df.describe()
    # pegamos uma descrição da tabela, que nos informa aspectos estatísticos

    clients_df_categoria = clients_df["Categoria"].value_counts()
    # contamos o número de cada elemento presente na coluna categoria

    clients_df_categoria_pct = clients_df["Categoria"].value_counts(normalize=True)
    # pegamos agora o percentual de presença de cada elemento

    for coluna in clients_df:  # automaticamente, em um for, pegamos as colunas da tabela
        gera_grafico_coluna(coluna, clients_df)


