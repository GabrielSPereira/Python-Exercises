valor = float(input("Digite o valor do empréstimo\n"))
parcela = int(input("Digite a quantidade de parcelas\n"))
if parcela <= 3:
    valor = valor * 0.06
elif parcela > 3 and parcela <= 6:
    valor = valor * 0.09
elif parcela > 6 and parcela <= 12:
    valor = valor * 0.22
else:
    valor = valor * 0.34

print("Valor do juros é",round(valor, 2))
