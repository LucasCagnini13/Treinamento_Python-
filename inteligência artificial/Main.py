import pandas as pd

tabela = pd.read_csv("clientes.csv")

print("Analise da base de dados")
print(tabela.info())

print("="*1000)
#verificar se a base de dados tem problemas e preparar dados para IA

from sklearn.preprocessing import LabelEncoder

codificador_profissao = LabelEncoder()
codificador_mix_credito = LabelEncoder()
codificador_comportamento_pagamento = LabelEncoder()

tabela["profissao"] = codificador_profissao.fit_transform(tabela["profissao"])

tabela["mix_credito"] = codificador_mix_credito.fit_transform(tabela["mix_credito"])

tabela["comportamento_pagamento"] = codificador_comportamento_pagamento.fit_transform(tabela["comportamento_pagamento"])

print("tabela com codificador: ")
print(tabela.info())

x = tabela.drop(columns=["id_cliente","score_credito"])
y = tabela["score_credito"]

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y)

#criar e treinar modelo de IA

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

#testar e escolher o melhor modelo de IA

previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

from sklearn.metrics import accuracy_score

print("precisão modelo arvore decisão: {}".format(accuracy_score(y_teste, previsao_arvoredecisao)))
print("precisão modelo knn: {}".format(accuracy_score(y_teste, previsao_knn)))

#o modelo arvore de decisão teve uma melhor precisão, então vamos usar ela para prever os scores de créditos de outros clientes

tabela_novos_clientes = pd.read_csv("novos_clientes.csv")

tabela_novos_clientes["profissao"] = codificador_profissao.transform(tabela_novos_clientes["profissao"])
tabela_novos_clientes["mix_credito"] = codificador_mix_credito.transform(tabela_novos_clientes["mix_credito"])
tabela_novos_clientes["comportamento_pagamento"] = codificador_comportamento_pagamento.transform(tabela_novos_clientes["comportamento_pagamento"])

previsoes = modelo_arvoredecisao.predict(tabela_novos_clientes)

print("previsão com novos clientes : ")
print(previsoes)





