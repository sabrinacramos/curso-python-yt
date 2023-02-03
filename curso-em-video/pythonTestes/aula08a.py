# --> IMPORT MATH - importa a biblioteca inteira

# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)

# print(f'A raiz de {num} é igual a {raiz}')

# ## PARA ARREDONDAR PARA CIMA USAR 'math.ceil()'
# print(f'A raiz de {num} é igual a {math.ceil(raiz)}')

# ## PARA ARREDONDAR PARA BAIXO USAR 'math.floor()'
# print(f'A raiz de {num} é igual a {math.floor(raiz)}')

# ------------------------------------------------------------

# --> FROM MATH IMPORT - importa coisas especificas

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é igual a {floor(raiz)}')
