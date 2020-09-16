# Questão 1. Uma empresa decidiu fazer um levantamento em relação aos candidatos 
# que se apresentarem para preenchi- mento de vagas em seu quadro de funcionários. 
# Supondo que você seja o programador dessa empresa, faça um programa que leia, para 
# cada candidato, a idade, o sexo (M ou F), e a experiência no serviço (S ou N). 
# Para encerrar a entrada de dados, digite a idade igual a zero. O programa também 
# deve calcular e mostrar:
# --- O número de candidatos do sexo feminino.
# --- O número de candidatos do sexo masculino.
# --- A idade média dos homens que já tem experiência no serviço.
# --- A porcentagem dos homens com mais de 45 anos entre o total dos homens.
# --- O número de mulheres com idade inferior a 21 anos e com experiência no serviço.
# --- A menor idade entre as mulheres que já tem experiência no serviço.

menorIdadeFem = 150
quantFem = quantExpFem = quantMasc = quantExpMasc = quantIdadeMasc = somaIdadeMasc = 0
while True:
    idade = int(input("Digite a sua idade\n"))
    if(idade == 0):
        break
    sexo = input("Digite o seu sexo (M ou F)\n")
    experiencia = input("Têm experiência no serviço (S ou N)\n")
    if(sexo == "F"):
        quantFem = quantFem + 1
        if(experiencia == "S"):
            if(menorIdadeFem > idade):
                menorIdadeFem = idade
            if(idade <= 21):
                quantExpFem = quantExpFem + 1
    if(sexo == "M"):
        quantMasc = quantMasc + 1
        if(experiencia == "S"):
            somaIdadeMasc = somaIdadeMasc + idade
            quantExpMasc = quantExpMasc + 1
        if(idade >= 45):
            quantIdadeMasc = quantIdadeMasc + 1
if somaIdadeMasc != 0 and quantExpMasc != 0:
    media = somaIdadeMasc / quantExpMasc
else:
    media = 0
if(quantFem == 0):
    menorIdadeFem = 0
print("O número de candidatos do sexo feminino:",quantFem,"\n")
print("O número de candidatos do sexo masculino:",quantMasc,"\n")
print("A idade média dos homens que já tem experiência no serviço:",media,"\n")
print("A porcentagem dos homens com mais de 45 anos entre o total dos homens:",quantIdadeMasc,"\n")
print("O número de mulheres com idade inferior a 21 anos e com experiência no serviço:",quantExpFem,"\n")
print("A menor idade entre as mulheres que já tem experiência no serviço:",menorIdadeFem,"\n")
