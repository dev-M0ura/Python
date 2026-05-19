valorC=float(input('Digite o valor da casa: '))
salario=float(input('Digite o seu salário: '))
anos=int(input('Digite em quantos anos ira pagar: '))
minimo= salario*30/100
entrada= 0
meses = anos*12
prestacoes = meses/(valorC-entrada)
print (f'Para pagar uma casa de {valorC:.2f} em {anos}')
print(f'A prestação sera de {prestacoes}')
if prestacoes <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Emprestimo negado')