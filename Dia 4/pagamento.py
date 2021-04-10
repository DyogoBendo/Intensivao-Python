from selenium import webdriver
import pandas as pd
import time
from IPython.display import display

def planilha():
    clients_df = pd.read_excel("Clientes Pagamento.xlsx", dtype={"Cliente": object})
    # indicamos que a coluna cliente deve ser lida como um objeto
    display(clients_df)


if __name__ == '__main__':
    navegador = webdriver.Chrome()
    navegador.get("https://acesso.pagseguro.uol.com.br/?_ga=2.266889414.912489655.1613164953-1814135879.1606321643")



