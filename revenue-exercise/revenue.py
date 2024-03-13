# Dado um vetor que guarda o valor de faturamento diário de
# uma distribuidora, faça um programa, na linguagem que 
# desejar, que calcule e retorne: O menor valor de faturamento ocorrido em um dia do mês,
# O maior valor de faturamento ocorrido em um dia do mês,
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open('revenue-exercise\dados.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = [registro['valor'] for registro in dados]

faturamento_diario = [valor for valor in faturamento_diario if valor != 0]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print("Menor valor de faturamento diário:", menor_faturamento)
print("Maior valor de faturamento diário:", maior_faturamento)
print("Número de dias com faturamento diário superior à média mensal:", dias_acima_media)
