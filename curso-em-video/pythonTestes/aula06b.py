# DESAFIO:
# 1 - CRIE UM PROGRAMA QUE LEIA DOIS NUMEROS E MOSTRE A SOMA ENTRE ELES.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

soma = n1 + n2
print(f'A soma vale {soma}')

# 2 - FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELA.

var1 = input('Digite algo: ')

print('ele é um numero?', var1.isnumeric())
print('ele é uma letra?', var1.isalpha())
print('ele esta em minusculo?', var1.islower())
print('ele esta em maiusculo?', var1.isupper())
