print('''=========================
    10 TERMOS DE UMA PA
=========================''')
termoUm=int(input('Digite o primeiro termo: '))
termoDois=int(input('Digite o segundo termo: '))
decimo=termoUm+(10-1)*termoDois
for c in range (termoUm, decimo+termoDois, termoDois):
    print(c, end=' -> ' )
print('ACABOU')