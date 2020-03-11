salario = float(input("Digite o seu salário\n"))
aumento = int(input("Digite o aumento\n"))
novo = salario + (salario*(aumento/100))
print("Seu novo salário é",novo,"após o aumento de",aumento,"%")