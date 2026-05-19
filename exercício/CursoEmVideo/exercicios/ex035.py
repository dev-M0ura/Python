reta1=float(input('Digite o comprimento: '))
reta2=float(input('Digite o comprimento: '))
reta3=float(input('Digite o comprimento: '))
if (reta1+reta2>reta3) and (reta1+reta3>reta2) and (reta2+reta3>reta1):
    print('pode fazer um triangulo')
else:
    print('não pode fazer um trinagulo')