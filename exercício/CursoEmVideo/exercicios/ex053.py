frase=str(input('Digite a frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
print(f'o inverso de {junto} é {inverso}')
if inverso==junto:
    print(f'é um palindromo')
else:
    print(f'Não é um palindromo')