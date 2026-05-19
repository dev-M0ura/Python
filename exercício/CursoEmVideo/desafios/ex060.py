from math import factorial
num=int(input('Digite seu numero: '))
fat=factorial(num)
cont=num
while cont>0:
    print(cont, end='')
    print(' x ' if cont>1 else ' = ', end='' )
    cont-=1
print (f'O fatorial de {num}! é {fat}')