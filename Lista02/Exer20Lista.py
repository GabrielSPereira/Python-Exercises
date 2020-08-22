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

    