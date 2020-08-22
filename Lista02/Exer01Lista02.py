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
