soma = 0
for c in range (1, 7):
    num=int(input(f'Digite o {c} Numero: '))
    if num%2==0:
        soma+=num
print(f'A soma dos números pares é {soma}')
