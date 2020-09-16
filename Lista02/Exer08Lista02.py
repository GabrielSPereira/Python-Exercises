# Questão 8. Faça um programa para calcular e exibir a quantidade de parcelas sem juros 
# e o valor de cada parcela, conforme o valor da compra digitado pelo usuário (incluindo 
# centavos – cuidado com o uso do tipo de dados correto).

valor = float(input("Digite o valor da compra\n"))
if valor <= 100.00:
    valor = valor / 2
    parcela = 2
elif valor > 100.00 and valor <= 200.00:
    valor = valor / 3
    parcela = 3
elif valor > 200.00 and valor <= 400.00:
    valor = valor / 4
    parcela = 4
else:
    valor = valor / 5
    parcela = 5

print("Valor das",parcela,"parcelas sem juros",round(valor, 2))
