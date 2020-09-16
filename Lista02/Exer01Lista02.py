# Questão 1. Faça um programa para calcular e exibir o desconto de INSS conforme 
# o valor do salário digitado pelo usuário (incluindo centavos – cuidado com o 
# uso do tipo de dados correto).

valor = float(input("Digite o valor do salário mínimo\n"))
if valor <= 600.00:
    valor = valor - (valor * 0.07)
elif valor > 600.00 and valor <= 800.00:
    valor = valor - (valor * 0.09)
elif valor > 800.00 and valor <= 1200.00:
    valor = valor - (valor * 0.09)
else:
    valor = valor - (valor * 0.11)

print("Valor líquido que irá receber é",round(valor, 2))
