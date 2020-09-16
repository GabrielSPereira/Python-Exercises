# Questão 20. Ler os valores de quatro notas escolares bimestrais de um aluno representadas 
# pelas variáveis N1, N2, N3, N4. Calcular a média aritmética (variável MD1) desse aluno 
# e apresentar a mensagem "APROVADO" se a média obtida for maior ou igual a 7. 
# Caso contrário, o programa deve solicitar a quinta nota (nota de exame, representada 
# pela variável NE) do aluno e calcular uma nova média aritmética (variável MD2) entre 
# a nota de exame e a primeira média aritmética. Se o valor da nova média for maior ou 
# igual a cinco, apresentar a mensagem "APROVADO EM EXAME". Caso contrário, apresentar a 
# mensagem "REPROVADO". Informar também, após a apresentação das mensagens, o valor 
# da média obtida pelo aluno.

n1 = float(input("Digite a N1\n"))
n2 = float(input("Digite a N2\n"))
n3 = float(input("Digite a N3\n"))
n4 = float(input("Digite a N4\n"))
md1 = (n1 + n2 + n3 + n4) / 4
if md1 >= 7:
    status = "APROVADO"
else:
    ne = float(input("Digite a NE\n"))
    md2 =  (n1 + n2 + n3 + n4 + ne) / 5
    md1 = md2
    if md2 >= 5:
        status = "APROVADO EM EXAME"
    else:
        status = "REPROVADO"
print("O resultado é",status,", pois sua média foi",md1)

    