#Escreva um programa na linguagem que desejar onde 
#calcule o percentual de representação que cada estado
# teve dentro do valor total mensal da distribuidora.

faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento_por_estado.values())

print("Percentual de representação por estado:")
for estado, faturamento in faturamento_por_estado.items():
    percentual = (faturamento / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")