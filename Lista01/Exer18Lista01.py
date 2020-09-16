# Questão 18. Elabore um programa que calcule o alcance de um projétil, dada a velocidade (Vo), 
# o ângulo (ang) entre o cano do canhão e o solo. A fórmula a ser utilizada é:
# --- S = (Vo Vo /g) sen(2ang), onde S é o alcance, g é a gravidade, ang é dado em graus, sendo necessário 
# converter para radianos.

import math
Vo = int(input("Digite o valor da velocidade\n"))
angulo = int(input("Digite o valor do ângulo em graus\n"))
angRad = math.sin(2 * math.radians(angulo))
alcance = (Vo*Vo / 9.81) * angRad
print("Alcance é", round(alcance, 2))