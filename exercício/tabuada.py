num=(int(input('Digite o numero que deseja ver a tabuada: ')))
cont=1
print('-'*30)
print('resultado dad tabuada')
print('-'*30)
while cont<=10:
    print(f'{num} x {cont:2}= {num*cont:2}')
    cont=cont+1
print('FIM')