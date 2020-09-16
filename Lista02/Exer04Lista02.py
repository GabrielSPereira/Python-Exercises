# Questão 4. Faça um programa para calcular e exibir o desconto de IR conforme o valor do 
# salário digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

valor = float(input("Digite o salário\n"))
if valor <= 1250.00:
    valor = 0
elif valor > 1250.00 and valor <= 1900.00:
    valor = valor * 0.11
elif valor > 1900.00 and valor <= 2700.00:
    valor = valor * 0.25
else:
    valor = valor * 0.275

print("Valor do desconto de IR é",round(valor, 2))
