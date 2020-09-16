# Questão 9. Faça um programa que leia quinze valores numéricos inteiros e no 
# final apresente o somatório e a média aritmética dos valores lidos.

soma = 0
for contador in range(1, 16):
    numero = int(input("Digite um número\n"))
    soma += numero
media = soma / 15
print("Média aritmética dos números",media)