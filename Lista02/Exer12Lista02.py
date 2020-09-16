# Questão 12. Faça um programa que determine se um dado número é par ou ímpar.

valor = int(input("Digite um número\n"))
if valor % 2 == 1:
    status = "ímpar"
else:
    status = "Par"
print("Esse número é",status)
