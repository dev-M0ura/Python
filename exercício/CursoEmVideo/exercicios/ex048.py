num=0
for c in range (1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        num+= c
print(f'a soma de todos os valores é {num}')