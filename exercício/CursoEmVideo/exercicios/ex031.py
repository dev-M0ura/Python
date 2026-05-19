distancia=float(input('Digite o distância em KM: '))
valor=float()
if (distancia<=200):
    valor=distancia*0.50
    print(f'voce ira pagar R${valor}')
else:
    valor=distancia*0.45
    print(f'voce ira pagar R${valor}')