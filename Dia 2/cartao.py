import pandas as pd
from IPython.display import display

if __name__ == '__main__':

    clients_df = pd.read_csv("ClientesBanco.csv", encoding="latin1")
    # recebemos os dados de uma tabela do tipo csv, que contém caracteres latinos

    clients_df = clients_df.drop("CLIENTNUM", axis=1)
    # apagamos uma coluna, chamada CLIENTNUM
    # a base original não é afetada

    display(clients_df)
