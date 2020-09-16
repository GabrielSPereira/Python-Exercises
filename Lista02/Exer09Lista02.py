# Questão 9. Faça um programa para calcular e exibir o desconto na compra do 
# cliente em uma farmácia, conforme o valor da compra do mesmo digitado pelo 
# usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).

valor = float(input("Digite o valor total de serviços\n"))
if valor <= 150.00:
    valor = valor * 0.05
elif valor > 150.00 and valor <= 300.00:
    valor = valor * 0.07
elif valor > 300.00 and valor <= 500.00:
    valor = valor * 0.10
else:
    valor = valor * 0.20

print("Valor do desconto é",round(valor, 2))
