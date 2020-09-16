# Questão 7. Elabore um programa que efetue a leitura de cinco números 
# inteiros, adicione-os a uma lista e mostre-a.

lista = []
for i in range(5):
    numero = int(input("Digite o um número\n"))
    lista.append(numero)
print(lista)