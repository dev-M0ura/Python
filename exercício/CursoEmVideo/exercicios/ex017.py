import math
cateO=float(input('tamanho do comprimento: '))
cate=float(input('tamanho do cateto: '))
hip= math.hypot(cateO, cate)
print(f'A hipotenusa de {cateO} e {cate} é {hip}')