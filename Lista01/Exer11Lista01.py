# Questão 11. Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; 
# mas, agora, todos incorporam essa palavra em seu vocabulário. Sabendo-se que 100 quilowatts de 
# energia custa um sétimo do salário mínimo, fazer um programa que receba o valor do salário mínimo e a 
# quantidade de quilowatts gasta por uma residência e calcule. Imprima:
# --- o valor em reais de cada quilowatt,
# --- o valor em reais a ser pago,
# --- o novo valor a ser pago por essa residência com um desconto de 10%.

salMin = float(input("Digite o valor do salário mínimo\n"))
quiloW = float(input("Digite a quantidade de quilowatt\n"))
valorQuilo = salMin / 700
valorPago = valorQuilo * quiloW
ValorDesc = valorPago - (valorPago* 0.1)
print("Valor de cada quilowatt é", round(valorQuilo, 2),", o valor pago",round(valorPago, 2),", e o valor pago descontado",round(ValorDesc, 2))