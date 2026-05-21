from random import randint
v=0
while True:
    player=int(input('Digite um numero: '))
    pc= randint(0, 10)
    total= player+pc
    tipo=' ' 
    while tipo not in 'PI':
        tipo=str(input('Par ou Impar: [P/I]')).strip().upper()[0]
    print(f'voce jogou {player} e o comutador jogou {pc} = {total}')
    if tipo =='P':
        if total%2==0:
            print('voce ganhou')
            v+=1
        else:
            print('voce perdeu')
            break
    elif tipo=='I':
        if total%2==1:
            print('voce ganhou')
            v+=1
        else:
            print('voce perdeu')
            break
    print('vamos jogar denovo')
print(f'voce venceu {v}vezes')


