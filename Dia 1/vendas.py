from IPython.display import display
import pandas as pd

if __name__ == '__main__':
    tabela_vendas = pd.read_excel("Vendas.xlsx")  # importando base de dados

    """
    Realizando o cálculo do faturamento das lojas
    """
    tabela_filtrada = tabela_vendas[["ID Loja", "Valor Final"]]
    # filtramos a tabela, pegando apenas essa duas colunas

    tabela_faturamento = tabela_filtrada.groupby("ID Loja").sum()
    # Agrupamos as lojas pelo nome, e somamos a coluna de valor final

    display(tabela_faturamento)
