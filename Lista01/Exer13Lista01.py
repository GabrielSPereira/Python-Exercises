# Questão 13. Dado um polígono convexo de n lados, podemos calcular o número de diagonais 
# diferentes (nd) desse polígono pela fórmula: nd = n * (n - 3) / 2. Fazer um programa que 
# leia quantos lados tem o polígono, calcule e escreva o número de diagonais diferentes (nd) do mesmo.

lados = int(input("Digite a quantidade de lados\n"))
nd = lados * (lados - 3) / 2
print("Quantidade de número de diagonais diferentes é", nd)