valor = int(input("Digite um ano\n"))
if valor % 400 == 0 or (valor % 4 == 0 and valor % 100 > 0):
    status = "Bissexto"
else:
    status = "Não é bissexto"
print("Esse ano é",status)
