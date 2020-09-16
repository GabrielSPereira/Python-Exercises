# Questão 10. Faça um programa que leia uma lista com dez caracteres, 
# e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = ['a','e','i','o','u']
lista = []
j = 0
for i in range(10):
    caracter = input("Digite um caracter\n")
    caracter = caracter.lower()
    if caracter in vogais:          
        pass
    else:
        lista.append(caracter)
        j+=1
print("Foram inseridas",j,"consoantes, são elas",lista)
