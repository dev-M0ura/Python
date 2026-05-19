num=int(input('Quantos termos: '))
term=0
term2=1
print(f'{term} -> {term2}', end='')
cont=3
while cont <=num:
        term3= term+term2
        print(f' -> {term3}', end='')
        term=term2
        term2=term3
        cont+=1
print(' FIM')