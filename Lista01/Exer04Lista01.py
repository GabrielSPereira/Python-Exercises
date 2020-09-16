# Questão 4. Faça um programa que receba o salário-base de um funcionário, calcule e 
# mostre o salário a receber, sabendo-se que esse funcionário tem gratificação de 5% 
# sobre o salário-base e paga imposto de 7% sobre salário-base.

salario = float(input("Digite o seu salário\n"))
aumento = salario*0.05
desconto = salario*0.07
novo = salario + aumento - desconto
print("Seu novo salário com os reajustes é",novo)