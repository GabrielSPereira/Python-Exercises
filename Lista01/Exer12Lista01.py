# Questão 12. Criar um programa que efetue o cálculo da hora aula líquida 
# (descontado o percentual de imposto) de um professor. Os dados fornecidos 
# serão: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS.

valor = float(input("Digite o valor do salário mínimo\n"))
num = float(input("Digite o número de aulas dadas no mês\n"))
inss = float(input("Digite o percentual de desconto do INSS\n"))
valorLiq = (valor * num) - ((valor * num) * (inss/100))
print("Valor líquido que irá receber é",round(valorLiq, 2))