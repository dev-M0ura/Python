maior=0
menor=0
for cont in range (1, 6):
    peso=float(input('Digite o seu peso: '))
    if cont ==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print(f'o maior peso foi {maior} e o menor foi {menor} ')