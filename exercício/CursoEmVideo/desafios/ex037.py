num=int(input('Digite um numero inteiro: ')) 
num2=int(input('[1] converter para binário \n[2] converter para hexadecimal \n[3]converter para octal \nsua opção: '))
if num2<=1:
    binario=bin(num)
    print(f'O número {num} em binário é {binario}')
elif num2==2:
    hexad=hex(num)
    print(f'O número {num} em hexadecimal é {hexad}')
elif num2==3:
    octal=oct(num)
    print(f'O número {num} em octal é {octal}')
else:
    print('falei de 1 a 3, não mais que isso seu burro')