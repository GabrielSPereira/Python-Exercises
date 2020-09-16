# Questão 9. Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária. 
# Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. Sabe-se que cada 
# operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado.

cheque1 = float(input("Digite o valor do primeiro cheque\n"))
cheque2 = float(input("Digite o valor do segundo cheque\n"))
salarioAt = (cheque1 + cheque2) - ((cheque1 * 0.038) + (cheque2 * 0.038))
print("Salario atual é",round(salarioAt, 2))