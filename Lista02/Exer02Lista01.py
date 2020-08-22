valor = float(input("Digite o valor de vendas\n"))
if valor <= 5000.00:
    valor = valor * 0.02
elif valor > 5000.00 and valor <= 10000.00:
    valor = valor * 0.05
elif valor > 10000.00 and valor <= 15000.00:
    valor = valor * 0.07
else:
    valor = valor * 0.09

print("Valor recebido de comissão",round(valor, 2))
