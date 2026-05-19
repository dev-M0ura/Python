num=int(input('Digite um numero: '))
tot=0
for c in range (1,num+1):
    if num%c==0:
        print('\033[34m', end='')
        tot+=1
    else:
        print('\033[31m', end='')
    print(c , end='')
print(f' o numero {num} foi divisivel {tot} vezes')
if tot==2:
    print(f'o numero {num} é primo ')
else:
    print(f'o numero {num} não é primo')
