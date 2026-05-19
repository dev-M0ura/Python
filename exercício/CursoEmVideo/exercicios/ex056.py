media=0
somaI=0
maiorI=0
velho=str()
mulher=0
for c in range (1, 5):
    nome=str(input('Digite seu nome: '))
    idade=int(input('Digite sua idade: '))
    sexo=str(input('sexo F/M: ')).upper()
    somaI+=idade
    if sexo == 'M':
        if idade>maiorI:
            maiorI=idade
            velho=nome
    elif sexo == 'F':
        if idade<25:
            mulher+=1
    else:
        print('Voce é uma gambiarra do diabo')
media=somaI/4
print(f'''o homem mais velho se chama {velho} com {maiorI}
á {mulher} mulheres com menos de 25
a media de idades é {media} ''')