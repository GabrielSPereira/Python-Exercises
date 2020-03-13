import math
Vo = int(input("Digite o valor da velocidade\n"))
angulo = int(input("Digite o valor do ângulo em graus\n"))
angRad = math.sin(2 * math.radians(angulo))
alcance = (Vo*Vo / 9.81) * angRad
print("Alcance é", round(alcance, 2))
