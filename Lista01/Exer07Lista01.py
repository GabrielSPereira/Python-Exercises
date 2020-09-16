# Questão 7. Elaborar um programa que calcule e apresente em metros por segundo o valor da 
# velocidade de um projétil que percorre uma distância em quilômetros a um espaço de tempo em minutos.

quilometro = float(input("Digite um valor em km/h\n"))
metro = quilometro * 16.667
print("Valor em pés",quilometro,", tranformado para metros",round(metro, 2))