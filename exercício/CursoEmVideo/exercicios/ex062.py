print ('Gerador de PA')
print('-='*10)
primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
termo=primeiro
cont=1
total=0
mais=10
while mais !=0:
    total+=mais
    while cont <=total:
        print(f'{termo}')
        termo+=razao
        cont+=1
    print('PAUSA')
    mais= int(input('Quanto termos voce quer mostras a mais: '))
print('FIM')