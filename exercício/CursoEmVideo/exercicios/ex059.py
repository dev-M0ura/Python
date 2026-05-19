from time import sleep
opcao=0
def valor ():
    valor1=int(input('Qual o primeiro valor?'))
    valor2=int(input('Qual o segundo valor?'))
    return valor1, valor2
valor1, valor2 = valor()

while opcao!=5:
    print('========================')
    sleep(1)
    opcao=int(input('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    Qual a sua opção: '''))
    if opcao==1:
        soma=valor1+valor2
        print(soma)
    elif opcao==2:
        mult=valor1*valor2
        print(mult)
    elif opcao==3:
        if valor1>valor2:
            maior=valor1
            print(f'o maior numero entre {valor1} e {valor2} é {maior}')
        elif valor1==valor2:
            print(f'os valores são  iguais')
        else:
            maior=valor2
            print(f'o maior numero entre {valor1} e {valor2} é {maior}')
    elif opcao==4:
       valor1, valor2 = valor()
    elif opcao>5:
        print('opcao invalida')
print('fim do programa')


