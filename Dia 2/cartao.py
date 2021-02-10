import pandas as pd
from IPython.display import display

if __name__ == '__main__':

    clients_df = pd.read_csv("ClientesBanco.csv", encoding="latin1")
    # recebemos os dados de uma tabela do tipo csv, que contém caracteres latinos

    clients_df = clients_df.drop("CLIENTNUM", axis=1)
    # apagamos uma coluna, chamada CLIENTNUM
    # a base original não é afetada

    info_df = clients_df.info()
    # pegamos informações sobre a tabela, informando o tipo de cada coluna, e se possuem linhas vazias

    display(info_df)

    clients_df = clients_df.dropna()
    # nós apagamos todas as linhas que possuem alguma célula vazia

    info_df = clients_df.info()
    display(info_df)
