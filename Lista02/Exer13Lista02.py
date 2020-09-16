# Questão 13. Faça um programa que simule uma calculadora com as quatro operações básicas (+, -, *, / ). 
# O programa deve solicitar ao usuário a entrada de dois operandos e da operação a ser executada, 
# na forma de menu. Dependendo da opção escolhida, deve ser executada a operação solicitada e 
# escrito seu resultado. Utilize uma variável do tipo inteiro para armazenar a operação e 
# utilize o comando caso para escolher a operação a ser executada a partir do operador.

valor1 = int(input("Digite um número\n"))
valor2 = int(input("Digite outro número\n"))
operacao = input("Escreva a operação\n")
if operacao == "Multiplicação":
    valor = valor1 * valor2
elif operacao == "Soma":
    valor = valor1 + valor2
elif operacao == "Subtração":
    valor = valor1 - valor2
elif operacao == "Divisão":
    valor = valor1 / valor2
else:
    valor = "Operação não reconhecida"
print("Resultado é:",valor)
