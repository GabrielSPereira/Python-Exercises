# Questão 5. Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
# --- O número digitado ao quadrado;
# --- O número digitado ao cubo;
# --- A raiz quadrada do número digitado;
# --- A raiz cúbica do número digitado;
# --- A soma do quadrado mais o cubo do número digitado.

num = float(input("Digite um número positivo\n"))
if(num > 0):
    quadrado = num ** 2
    cubo = num ** 3
    raizQ = num ** (1/2)
    raizC = num ** (1/3)
    soma = quadrado + cubo
    print("Número digitado",num,", quadrado dele",quadrado,", cubo dele",cubo,", raíz dele",raizQ,", raíz cúbica dele",raizC,"e a soma do quadrado e cubo",soma)
else:
    print("Apenas números positivos e maiores que zero")


