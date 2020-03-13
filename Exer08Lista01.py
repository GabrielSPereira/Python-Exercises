horas = float(input("Digite a quantidade de horas trabalhadas\n"))
salarioMin = float(input("Digite o salário mínimo\n"))
salHora = salarioMin/2
salarioBru = salHora * horas
imposto = salarioBru * 0.03
salarioRec = salarioBru - imposto
print("Salário a receber será",round(salarioRec, 2))
