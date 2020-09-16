# Questão 14. Faça um programa que leia as repostas de três questões de múltipla 
# escolha (a, b, c, d). Em seguida, leia o gabarito dessas questões, ou seja, as 
# respostas corretas. Depois, compare as respostas dadas com as do gabarito e indique 
# quantas respostas estão corretas

valor1 = input("Raíz de 49 é\n a - 7\n b - 8\n c - 4\n d - 5\n")
valor2 = input("\n3 vezes 7 é\n a - 27\n b - 21\n c - 26\n d - 22\n")
valor3 = input("\nMelhor cidade\n a - Bragança Paulista\n b - Atibaia\n c - Nazaré Paulista\n d - Itatiba\n")
resultado = 0
if valor1 == "a":
    resultado = resultado + 1
if valor2 == "b":
    resultado = resultado + 1
if valor3 == "a":
    resultado = resultado + 1
print("Você acertou:",resultado,"questões")
