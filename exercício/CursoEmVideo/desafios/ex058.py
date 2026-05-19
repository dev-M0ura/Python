import random
pc = random.randint(0,10)
acerto=False
while not acerto:
    player = int(input('Qual o seu palpite?'))
    if player==pc:
        acerto=True
    elif player>pc:
        print('menos, tente novamente')
    else:
        print('mais, tente novamente')
print('Voce acertou')