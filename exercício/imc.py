peso=float(input('Qual o seu peso?'))
altura=float(input('Qual a sua altura?'))
imc=peso/(altura*altura)
if imc < 18.5:
    print(f'seu imc é {imc:.2f} abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print(f'seu imc é {imc:.2f} peso normal')
elif imc >= 25 and imc <= 29.9:
    print(f'seu imc é {imc:.2f} peso sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print(f'seu imc é {imc:.2f} obesidade grau 1')
elif imc >= 35 and imc <= 39.9:
    print(f'seu imc é {imc:.2f} obesidade grau 2')
else:
    print(f'seu imc é {imc:.2f} obesidade grau 3')