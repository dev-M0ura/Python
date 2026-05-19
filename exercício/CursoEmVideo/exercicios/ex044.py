from time import sleep
valor=float(input('Digite o preço do produto: '))
formaP=int(input('Foma de pagamento: \n 1 [Dinheiro] \n 2 [Cartão (á vista)] \n 3 [2x no cartão] \n Digite o tanto de vezes 3x ou mais\n '))
novoV=float()
print('=====PROCESSANDO=====')
sleep(1)
if formaP<=1:
    novoV= valor*0.1
    print(f'você irá pagar {novoV}')
elif formaP==2:
    novoV= valor*0.05
    print(f'você irá pagar {novoV}')
elif formaP==3:
    print(f'você irá pagar {valor}')
else:
    print('INVALIDO')

