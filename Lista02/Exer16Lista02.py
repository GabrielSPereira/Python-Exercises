# Questão 16. Dado um ano d.C. (depois de Cristo), identifique se este é um ano bissexto ou não. 
# Considere que para o ano ser bissexto basta que seja divisível por 400. Caso contrário, 
# este precisará ser divisível por 4 e não ser divisível por 100.

valor = int(input("Digite um ano\n"))
if valor % 400 == 0 or (valor % 4 == 0 and valor % 100 > 0):
    status = "Bissexto"
else:
    status = "Não é bissexto"
print("Esse ano é",status)
