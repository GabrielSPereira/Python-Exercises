salMin = float(input("Digite o valor do salário mínimo\n"))
quiloW = float(input("Digite a quantidade de quilowatt\n"))
valorQuilo = salMin / 700
valorPago = valorQuilo * quiloW
ValorDesc = valorPago - (valorPago* 0.1)
print("Valor de cada quilowatt é", round(valorQuilo, 2),", o valor pago",round(valorPago, 2),", e o valor pago descontado",round(ValorDesc, 2))

