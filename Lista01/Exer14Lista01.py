# Questão 14. Sabendo que a relação entre vértices, arestas e faces de um objeto 
# geométrico é dada pela fórmula: vértices + faces = arestas + 2. Elabore um programa 
# que calcule o número de vértices de um objeto geométrico genérico. A entrada será o 
# número de faces e arestas (dadas por um número inteiro e positivo) e a saída será o número de vértices.

face = int(input("Digite a quantidade de faces\n"))
aresta = int(input("Digite a quantidade de arestas\n"))
if(face > 0 and aresta > 0):
    vertices  = aresta - face + 2
    print("Número de vértices", vertices)
else:
    print("Apenas números inteiros e positivos")