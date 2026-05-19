import random
aluno1=input('Digite o nome: ')
aluno2=input('Digite o nome: ')
aluno3=input('Digite o nome: ')
aluno4=input('Digite o nome: ')
lista= [aluno1, aluno2,aluno3,aluno4]
random.shuffle(lista)

print(f'o a ordem sera: \n {lista} ')