# Questão 21. Escreva um programa que solicite ao usuário dois números e apresente na 
# tela os resultados das operações aritméticas (soma, subtração, multiplicação, divisão, 
# resto da divisão, exponenciação, radiciação).

x = float(input("Digite o valor de X\n"))
y = float(input("Digite o valor de Y\n"))
print("Valor da soma é",x + y)
print("\nValor da subtração é",x - y)
print("\nValor da multiplicação é",x * y)
print("\nValor da divisão é",x / y)
print("\nValor do resto da divisão é",x % y)
print("\nValor da exponenciação é",x ** y)
print("\nValor da radiação é",x ** (1/y))