
while True:
    num=int(input('voce que a tabuada de qual valor: '))
    if num<0:
        break
    cont=1
    for i in range(1, 11):
        print(f'{num} x {cont} = {num*cont}')
        cont+=1

print('fim')    

