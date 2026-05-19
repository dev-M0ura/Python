from datetime import date
maiorI=0
menorI=0
for c in range (1, 8):
    nasc=int(input('Digite seu ano de nascimento: '))
    atual= date.today().year
    nasc= atual-nasc
    if nasc<18:
        menorI= menorI+1
    else:
        maiorI=maiorI+1
print(f'{menorI} pessoas menor de idade')
print(f'{maiorI} pessoas maior de idade')

