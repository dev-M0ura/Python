from time import sleep
from random import randint
itens= ('Pedra', 'Papel', 'Tesoura')
player=int(input('[0] Pedra \n1] Papel \n[2] Tesoura \nQual a sua jogada: '))
pc=randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*20)
print(f'Jogador jogou {itens[player]} ')
print(f'Computador jogou {itens[pc]}')
print('-='*20)
if player==pc:
    print('Empate')
elif player==0:
    if pc==1:
        print ('COMPUTADOR VENCEU')
    elif pc==2:
        print ('PLAYER VENCEU')
elif player==1:
    if pc == 2:
        print ('COMPUTADOR VENCEU')
    elif pc == 0:
        print ('COMPUTADOR VENCEU')
elif player==2:
    if pc == 1:
        print ('JOGADOR VENCEU')
    elif pc == 0:
        print ('COMPUTADOR VENCEU')
else:
    print('JOGADA INVALIDA')