# Questão 19. Efetuar o cálculo e apresentar o valor de uma prestação de um 
# bem em atraso, utilizando a fórmula:
# --- prestacao = valor + (valor (taxa / 100) tempo)

valor = float(input("Digite o valor da prestação\n"))
taxa = float(input("Digite o valor da taxa\n"))
tempo = int(input("Digite o valor da tempo (dia)\n"))
prestacao =  valor + (valor * (taxa/100) * tempo)
print("Valor da prestacao, com ",tempo," dias de atraso é ",prestacao)