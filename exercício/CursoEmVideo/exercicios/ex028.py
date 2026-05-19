import random
num=random.randint(0, 5)
num1=int(input('Digite um numero: '))
if num1 == num:
    print('voce acertou')
else:
    print(f'voce errou,o computador venceu, o numero era {num}')
print('fim')
