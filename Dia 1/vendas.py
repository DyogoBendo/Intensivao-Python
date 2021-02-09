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

    tabela_faturamento = tabela_faturamento.sort_values(by="Valor Final", ascending=False)
    # ordenamos os valores da tabela a partir de:
    # 1: qual coluna
    # 2: de forma crescente ou descrescente

    display(tabela_faturamento)

    tabela_quantidade_venda = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
    # pegamos cada loja, agora queremos ver a quantidade de produtos vendido em cada uma delas

    tabela_quantidade_venda = tabela_quantidade_venda.sort_values(by="Quantidade")
    display(tabela_quantidade_venda)



