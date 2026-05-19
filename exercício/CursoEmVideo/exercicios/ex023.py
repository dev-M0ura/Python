num=int(input('Digite um numero de 1 a 9999: '))
uni = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'unidade {uni}')
print(f'dezena {dezena}')
print(f'centena {centena}')
print(f'milhar {milhar}')