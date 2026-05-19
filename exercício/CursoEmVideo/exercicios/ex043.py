import time
peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
imc =  peso/(altura**2)
print('estamos calculando, aguarde')
time.sleep(1)
if imc<18.5:
    print(f'seu imc é {imc:.2f}, você está abaixo do peso')
elif imc>=18.5 and imc<25:
    print(f'seu imc é {imc:.2f}, você está no peso ideal')
elif imc>=25 and imc<30:
    print(f'seu imc é {imc:2f}, você está sobrepeso')
elif imc>=30 and imc<=40:
    print(f'seu imc é {imc:.2f}, você está obeso')
else:
    print(f'seu imc é {imc:.2f}, você esta em obesidade mórbida')