salario=float(input('Digite seu salário: '))
bonus=float()
if (salario>1250):
    bonus=salario*0.1
    salario= bonus+salario
    print(f'seu salario ira ficar R${salario}')
else:
    bonus=salario*0.15
    salario=bonus+salario
    print(f'seu salário ira ficar R${salario}')