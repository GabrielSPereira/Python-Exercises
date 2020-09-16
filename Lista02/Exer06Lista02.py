# Questão 6. Faça um programa para calcular e exibir o desconto na compra do cliente, 
# conforme o valor da compra do mesmo digitado pelo usuário (incluindo centavos – 
# cuidado com o uso do tipo de dados correto).

valor = float(input("Digite o valor da compra\n"))
if valor <= 50.00:
    valor = valor * 0.05
elif valor > 50.00 and valor <= 100.00:
    valor = valor * 0.08
elif valor > 100.00 and valor <= 150.00:
    valor = valor * 0.12
else:
    valor = valor * 0.15

print("Valor do desconto é",round(valor, 2))
