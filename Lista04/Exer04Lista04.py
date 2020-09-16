# Questão 4. Elaborar um programa que a partir da digitação de uma frase, 
# o programa informe quantos espaços em branco e quantos são, e quantas 
# vezes aparecem cada uma das vogais a, e, i, o, u.

frase = input("Digite uma frase\n")
frase = frase.lower()
vogais = ['a','e','i','o','u']
j = 0
k = 0
for i in frase:
    if i in vogais:          
        j+=1
    if i in " ":
        k+=1
print(j)
print(k)