valor = float(input("Digite o valor do salário mínimo\n"))
num = float(input("Digite o número de aulas dadas no mês\n"))
inss = float(input("Digite o percentual de desconto do INSS\n"))
valorLiq = (valor * num) - ((valor * num) * (inss/100))
print("Valor líquido que irá receber é",round(valorLiq, 2))