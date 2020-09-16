# Questão 18. Efetuar a leitura de dois valores numéricos inteiros representados pelas 
# variáveis A e B e apresentar o resultado da diferença do maior valor pelo menor.

a = int(input("Digite um número\n"))
b = int(input("Digite outro número\n"))
if a > b:
    resultado = a - b 
else:
    resultado = b - a
print("O resultado é",resultado)
