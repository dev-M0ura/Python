num=0
soma=0
while num!=999:
    num=int(input('Digite um número: '))
    if num==999:
        break
    soma+=num
print(f'A soma dos números digitados é {soma}.')