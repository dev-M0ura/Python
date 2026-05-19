from datetime import date
ano=int(input('Digite seu ano de nascimento: '))
atual=date.today().year
idade= atual-ano
if idade<=17:
    idade= 18-idade
    print(f'faltam {idade} para voce se alistar')
elif idade>18:
    idade= idade-18
    print(f'já passou {idade} anos desde que voce tinha de se alistar')
else:
    print('está na hora de se alistar')