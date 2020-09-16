# Questão 11. Faça um programa que leia um número inteiro e diga se este é positivo, negativo ou zero.

valor = int(input("Digite um número\n"))
if valor < 0:
    status = "Negativo"
elif valor == 0:
    status = "Zero"
else:
    status = "Positivo"
print("Esse número é",status)
