veloci=float(input('Digite a velocidade do carro: '))
multa=float()
if (veloci>80):
    multa = (veloci-80)*7
    print(f'voce foi multado em R${multa}')
else:
    print('voce esta livre, dirija com segurança')