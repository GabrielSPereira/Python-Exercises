# Questão 3. Faça um programa que receba o número sorteado por um dado em vinte jogadas. 
# Exibir os números sorteados e a frequência com que cada um aparece.

sorteioUm = 0
sorteioDois = 0
sorteioTres = 0
sorteioQuatro = 0
sorteioCinco = 0
sorteioSeis = 0
for item in range(20):
    dado = int(input("Digite o número sorteado\n"))
    print("Número sorteado foi",dado)
    if dado == 1:
        sorteioUm = sorteioUm + 1
    elif dado == 2:
        sorteioDois = sorteioDois + 1
    elif dado == 3:
        sorteioTres = sorteioTres + 1
    elif dado == 4:
        sorteioQuatro = sorteioQuatro + 1
    elif dado == 5:
        sorteioCinco = sorteioCinco + 1
    elif dado == 6:
        sorteioSeis = sorteioSeis + 1
print("O número 1 foi sorteado",sorteioUm,"vezes\n")
print("O número 2 foi sorteado",sorteioDois,"vezes\n")
print("O número 3 foi sorteado",sorteioTres,"vezes\n")
print("O número 4 foi sorteado",sorteioQuatro,"vezes\n")
print("O número 5 foi sorteado",sorteioCinco,"vezes\n")
print("O número 6 foi sorteado",sorteioSeis,"vezes\n")