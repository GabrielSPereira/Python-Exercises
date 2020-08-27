dicionario = {}
while True:
    nome = input("Digite o seu nome\n")
    if nome == "":
        break
    nota1 = float(input("Digite a nota 1\n"))
    nota2 = float(input("Digite a nota 2\n"))

    dicionario[nome] = [nota1, nota2]
while True:
    nome = input("Digite um nome para ver a média\n")
    if nome == "":
        break
    if nome in dicionario:
        media = (dicionario[nome][0] + dicionario[nome][1])/2
        print("Média do nome",nome,"é",media)
    else:
        print("Nome não encotrado")
