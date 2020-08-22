valor = float(input("Digite o valor total de serviços\n"))
if valor <= 5000.00:
    valor = valor * 0.04
elif valor > 5000.00 and valor <= 10000.00:
    valor = valor * 0.06
elif valor > 1000.00 and valor <= 20000.00:
    valor = valor * 0.13
else:
    valor = valor * 0.16

print("Valor do imposto de ISS",round(valor, 2))
