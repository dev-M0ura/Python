#Calcula a media e situação do aluno
#solicita os nome e notas
nome =str(input('Qual o seu nome?'))
nota=float(input('digite sua primeira nota: '))
nota2=float(input('digite sua segunda nota: '))
nota3=float(input('digite sua terceira nota: '))
nota4=float(input('digite sua quarta nota: '))

#calcula média
media=(nota+nota2+nota3+nota4)/4
print(f'Olá, {nome}, sua media final é igual a {media:.2f}')

#verifica a situação
if media >= 7:
    print(f'Parabéns, {nome}, voce foi APROVADO')
else:
    print(f'{nome}, voce foi reprovado')
