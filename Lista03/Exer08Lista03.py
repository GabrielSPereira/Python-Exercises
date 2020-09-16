# Questão 8. Faça um programa que leia valores positivos inteiros até que um valor 
# negativo seja informado. Ao final devem ser apresentados o maior e o menor 
# valores informados pelo usuário.

maior = menor = contador = 0
while True:
    valor = int(input("Digite um valor\n"))
    if valor < 0:
        break
    if contador == 0:
        maior = valor
        menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    contador +=1
print("Maior valor:",maior,"\n")
print("Menor valor:",menor)
