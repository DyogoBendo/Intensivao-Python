from IPython.display import display
import pandas as pd


def enviar_email(nome_loja, tabela):
    import smtplib
    import email.message

    server = smtplib.SMTP('smtp.gmail.com:587')
    corpo_email = f"""
    <p> Prezados, </p>
    <p> Segue relatório de vendas </p>
    {tabela.to_html()}  # convertendo tabela em html
    <p> Qualquer dúvida estou a disposição</p>
    """

    msg = email.message.Message()
    msg['Subject'] = f"Relatório de Vendas - {nome_loja}"

    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = 'dyogo.bendo.testes@gmail.com'
    msg['To'] = 'dyogoromagnabendo@gmail.com'
    password = "####"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


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

    tabela_quantidade_venda = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
    # pegamos cada loja, agora queremos ver a quantidade de produtos vendido em cada uma delas

    tabela_quantidade_venda = tabela_quantidade_venda.sort_values(by="Quantidade")

    ticket_medio = tabela_faturamento["Valor Final"] / tabela_quantidade_venda["Quantidade"]
    # ticket medio é o faturamento pela quantidade de produtos vendidos

    ticket_medio = ticket_medio.to_frame()
    # convertemos o ticket medio em uma tabela

    ticket_medio = ticket_medio.rename(columns={0: "Ticket Medio"})  # renomeado a coluna com nome 0

    tabela_completa = tabela_faturamento.join(tabela_quantidade_venda).join(ticket_medio)
    # juntamos todas as tabelas

    lista_lojas = tabela_vendas["ID Loja"].unique()
    # pegamos cada valor unico da coluna ID Loja

    for loja in lista_lojas:
        tabela_loja = tabela_vendas.loc[tabela_vendas["ID Loja"] == loja, ["ID Loja", "Quantidade", "Valor Final"]]
        #         # definimos as linhas e colunas que queremos

        tabela_loja = tabela_loja.groupby("ID Loja").sum()

        tabela_loja["Ticket Medio"] = tabela_loja["Valor Final"] / tabela_loja["Quantidade"]
        # Criamos a coluna Ticket Medio

        enviar_email(loja, tabela_loja)

    enviar_email("Diretoria", tabela_faturamento)





