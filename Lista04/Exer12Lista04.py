# Questão 12. Elabore um programa que efetue a leitura de quatro notas reais de
# 10 alunos, calcule e armazene em uma lista, a média de cada aluno, imprima o 
# número de alunos com média maior ou igual a 7.0.

lista = []
k = 0
for i in range(1,11):
    soma = 0
    for j in range(1,5):
        nota = float(input("Digite a "+str(j)+"ª nota do aluno "+str(i)+"\n"))
        soma = soma + nota 
    media = soma/4
    lista.append(media)
    if media >= 7:
        k+=1
print("A média dos 10 alunos são",lista,", sendo",k,"acima da média")