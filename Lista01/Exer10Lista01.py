# Questão 10. Pedro comprou um saco de ração com peso em quilos. Pedro possui dois 
# gatos para os quais fornece a quantidade de ração em gramas. Faça um programa 
# que receba o peso do saco de ração e a quantidade de ração fornecida para cada 
# gato. Calcule e mostre quanto restará de ração no saco após cinco dias.

racaoKg = float(input("Digite a quantidade de ração em kilos\n"))
gato1 = float(input("Digite a quantidade de ração para o gato 1 em gramas\n"))
gato2 = float(input("Digite a quantidade de ração para o gato 2 em gramas\n"))
quant = (racaoKg * 1000) - ((gato1 + gato2)* 5)
print("Restará de ração",round(quant, 2))
