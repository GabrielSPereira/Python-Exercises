# Questão 13. Faça um programa que carregue uma lista com os modelos de cinco carros 
# (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo 
# desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 
# Calcule e mostre:
# --- O modelo do carro mais econômico;
# --- Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma 
# distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe 2,25 o litro.

carros = ['Fusca','Gol','Vectra','Uno','Amarok']
consumo = [20.0,18.0,9.5,15.0,5.7]
economico = 9999
j = 0
for i in consumo:    
    print(j+1,"-",carros[j],"-",i,"-",round(1000/i,1),"litros - R$",round(1000/i*2.25,1))
    if i < economico:
        economico = i
        carro = j
    j+=1
print("O menor consumo é do",carros[carro])