import time
lado=float(input('Digite o comprimento do primeiro lado: '))
lado2=float(input('Digite o comprimento do segundo lado: '))
lado3=float(input('Digite o comprimento do terceiro lado: '))
print('=====PROCESSANDO=====')
time.sleep(2)
if lado<lado2+lado3 and lado2<lado+lado3 and lado3<lado+lado2:
    print('os seguimentos acima podem formar um triangulo')
    print('=====PROCESSANDO QUAL TRIANGULO IRA FORMAR=====')
    time.sleep(2)
    if lado==lado2 and lado==lado3 and lado2==lado3:
        print('é um triangulo equilatero, pois todos os lados são iguais')
    elif lado==lado2 or lado2==lado3 or lado==lado3:
        print('é um triangulo isósceles, pois tem dois lados iguais')
    else:
        print('é um triangulo escaleno, pois todos os lados são diferentes')
else:
    print('os seguimentos acima não podem formar um triangulo')













