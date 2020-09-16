# Questão 20. Escreva um programa que calcule e exiba na tela o perímetro e área de uma 
# circunferência. Dados: area = Pi raio ** 2, perimetro = 2 Pi * raio.

raio = float(input("Digite o valor do raio\n"))
pi =  3.1415926535897932384626357839340399511415560167917
area = pi * (raio ** 2)
perimetro = 2 * pi * raio
print("Valor da área é",round(area, 2),"e o valor do perímetro é",round(perimetro, 2))