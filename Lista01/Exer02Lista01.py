# Questão 2. Faça um programa que receba três notas e seus respectivos pesos, 
# calcule e mostre a média ponderada dessas notas. Exiba, as notas, seus respectivos pesos e a média.

N1 = float(input("Digite a nota 1\n"))
P1 = int(input("Digite o peso 1\n"))
N2 = float(input("Digite a nota 2\n"))
P2 = int(input("Digite a peso 2\n"))
N3 = float(input("Digite a nota 3\n"))
P3 = int(input("Digite a peso 3\n"))
media = (N1*(P1/10)) + (N2*(P2/10)) + (N2*(P2/10))
print("Nota 1 é",N1,"de peso",(P1/10),"Nota 2 é",N2,"de peso",(P2/10),"Nota 1 é",N3,"de peso",(P3/10))
print(f"\nE sua média é {media:.1f}")
