# Questão 16. Elabore um programa que calcule e exiba a média aritmética de 5 números ( k, x, y, z, w).

k = float(input("Digite o valor de K\n"))
x = float(input("Digite o valor de X\n"))
y = float(input("Digite o valor de Y\n"))
z = float(input("Digite o valor de Z\n"))
w = float(input("Digite o valor de W\n"))
media = (k + x + y + z + w)/5
print("Valor da media de todos é", round(media, 2))