# Questão 3. Faça um programa que receba o salário de um funcionário e o percentual 
# de aumento, calcule e mostre o valor do aumento e o novo salário.

salario = float(input("Digite o seu salário\n"))
aumento = int(input("Digite o aumento\n"))
novo = salario + (salario*(aumento/100))
print("Seu novo salário é",novo,"após o aumento de",aumento,"%")