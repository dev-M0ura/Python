sexo =input('Informe o sexo [M/F]: ').strip().upper()
while sexo not in 'MF':
        sexo = input('Dados invalidos. Por favor informe o sexo [M/F]: ').strip().upper()
print(f'sexo {sexo} regidtrsdo com sucesso')
