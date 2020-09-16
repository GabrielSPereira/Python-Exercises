# Questão 15. Elabore um programa que permita a entrada de dois valores ( x, y ), 
# troque seus valores entre si e então exiba os novos resultados.

x = int(input("Digite o valor de X\n"))
y = int(input("Digite o valor de Y\n"))
aux = x
x = y
y = aux
print("Valor de X agora é",x, "e o valor de Y agora é",y)