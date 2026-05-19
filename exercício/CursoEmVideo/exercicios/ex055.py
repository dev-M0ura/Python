maiorI=0
menorI=0
for cont in range (1, 6):
    idade=int(input('Digite a sua idade: '))
    if cont == 1:
        maiorI=idade
        menorI=idade
    else:
        if idade>maiorI:
            maiorI=idade
        if idade<menorI:
            menorI=idade
print(maiorI, menorI)