massa = float(input("Digite a sua massa\n"))
altura = float(input("Digite a sua altura\n"))
imc = massa / (altura * altura)
if imc < 17.00:
    status = "Muito abaixo do peso"
elif imc >= 17.00 and imc < 18.50:
    status = "Abaixo do pesoo"
elif imc >= 18.50 and imc < 25.00:
    status = "Peso normal"
elif imc >= 25.00 and imc < 30.00:
    status = "Acima do peso"
elif imc >= 30.00 and imc < 35.00:
    status = "Obesidade I"
elif imc >= 35.00 and imc < 40.00:
    status = "Obesidade II"
else:
    status = "Obesidade III (mórbida)"
print("O seu IMC é",status)
