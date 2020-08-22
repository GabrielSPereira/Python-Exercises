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
