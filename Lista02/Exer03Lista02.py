valor = float(input("Digite o valor do produto\n"))
tipo = input("Digite o tipo do produto\n")
if tipo == "Cesta Básica":
    valor = 0
elif tipo == "Eletrônicos":
    valor = valor * 0.25
elif tipo == "Serviços":
    valor = valor * 0.18
else:
    valor = valor * 0.12

print("Valor do imposto é",round(valor, 2))
