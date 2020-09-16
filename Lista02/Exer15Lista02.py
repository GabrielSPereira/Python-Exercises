# Questão 15. Faça um programa que leia três valores que representam os lados de um triângulo. 
# Primeiramente, verifique se os lados podem formar um triângulo ( a soma de dois lados não 
# pode ser menor que o terceiro lado ). Caso possa formar um triângulo, indique se este é 
# equilátero, isósceles ou escaleno.

valor1 = int(input("Digite um lado\n"))
valor2 = int(input("Digite outro lado\n"))
valor3 = int(input("Digite outro lado\n"))
if (valor1 + valor2) < valor3 or (valor1 + valor3) < valor2 or (valor2 + valor3) < valor1:
    resultado = "Não é um triângulo"
elif valor1 == valor2 and valor1 == valor3:
    resultado = "Triângulo Equilátero"
elif (valor1 == valor2 and valor1 != valor3) or (valor2 == valor3 and valor1 != valor3) or (valor1 == valor3 and valor2 != valor3):
    resultado = "Triângulo Isósceles"
else:
    resultado = "Triângulo Escaleno"
print("Resultado é:",resultado)
