palavra = 'iai nao'
vogais = ['a','e','i','o','u']
dicionario = {}
for i in vogais:
    if i in palavra:
        dicionario[i] = palavra.count(i)
print(dicionario)


