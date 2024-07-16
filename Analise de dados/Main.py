import pandas

tabela = pandas.read_csv("cancelamentos.csv")

print(tabela)

print("="*10000)

#corrigir os erros da base de dados, colunas vazias e informações inúteis

tabela = tabela.drop(columns=["CustomerID"])
tabela = tabela.dropna()

print(tabela.info())

print("="*1000)
#ver quantas pessoas cancelaram o plano

print("quantas pessoas que cancelaram: ")
print(tabela["cancelou"].value_counts())

#montar gráficos e comparar a coluna de cancelamento com outras colunas

import plotly.express as px

for coluna in tabela.columns:

    print(px.histogram(tabela,x = coluna, color="cancelou"))

# clientes do contrato mensal TODOS cancelam
    # ofercer desconto nos planos anuais e trimestrais
# clientes que ligam mais do que 4 vezes para o call center, cancelam
    # criar um processo para resolver o problema do cliente em no máximo 3 ligações
# clientes que atrasaram mais de 20 dias, cancelaram
    # política de resolver atrasos em até 10 dias (equipe financeira)

#simulação de como ficaria só cancelamentos sem os problemas encontrados na analise

tabela = tabela[tabela["duracao_contrato"] != "monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

print(tabela["cancelou"].value_counts())

print(tabela["cancelou"].value_counts(normalize=True))

