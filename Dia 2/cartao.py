import pandas as pd
from IPython.display import display

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

    display(clients_df_categoria)

    clients_df_categoria_pct = clients_df["Categoria"].value_counts(normalize=True)
    # pegamos agora o percentual de presença de cada elemento

    display(clients_df_categoria_pct)
