# Questão 12. Construa uma função que receba uma string como parâmetro 
# e devolva outra string com os carateres emba- ralhados. Por exemplo: 
# se função receber a palavra python, pode retornar npthyo, ophtyn ou 
# qualquer outra combinação possível, de forma aleatória. Padronize em 
# sua função que todos os caracteres serão devolvidos em caixa alta ou 
# caixa baixa, independentemente de como foram digitados.

import random

def embaralha(palavra):
    shuffled = list(palavra.lower())
    random.shuffle(shuffled)
    shuffled = "".join(shuffled)
    print("A palavra embaralhada é",shuffled,"\n")
palavra = input("Digite uma palavra\n")
embaralha(palavra)
