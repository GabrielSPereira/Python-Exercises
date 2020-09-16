# Questão 8. Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo. 
# Calcule e mostre o salário a receber seguindo as regras abaixo:
# --- a hora trabalhada vale a metade do salário mínimo;
# --- o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
# --- o imposto equivale a 3% do salário bruto;
# --- o salário a receber equivale ao salário bruto menos o imposto.

horas = float(input("Digite a quantidade de horas trabalhadas\n"))
salarioMin = float(input("Digite o salário mínimo\n"))
salHora = salarioMin/2
salarioBru = salHora * horas
imposto = salarioBru * 0.03
salarioRec = salarioBru - imposto
print("Salário a receber será",round(salarioRec, 2))
