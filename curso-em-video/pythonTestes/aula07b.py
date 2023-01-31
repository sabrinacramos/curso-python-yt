# DESAFIOS
# 1 - FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

# n1 = int(input('digite um número inteiro: '))
# n2 = 1

# soma = n1 + n2
# sub = n1 - n2

# print(f'Sucessor {soma} \nAntesessor {sub}')

# -------------------------------------------------------------------------------------------------------------

# 2 - CRIE UM ALGORITIMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA 

# numero = int(input('Digite um número: '))
# dobro = numero * 2
# triplo = numero * 3
# raiz = numero ** 0.5

# print(f'O número digitado foi {numero}, o drobro dele é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.2f}.')

# -------------------------------------------------------------------------------------------------------------

# 3 - DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO. CALCULE E MOSTRE SUA MÉDIA

# nomeAluno = input('Nome do aluno: ')
# quantidadeNotas = int(input('Digite a quantidade de notas: '))

# humanas = float(input('Nota humanas: '))
# exatas = float(input('Nota exatas: '))

# media = (humanas + exatas) / quantidadeNotas

# print(f'A media do/a {nomeAluno} é {media}')

# -------------------------------------------------------------------------------------------------------------

# 4 - ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS 

# metros = float(input('Digite o tamanho em métros: '))

# cm = metros * 100
# mm = metros * 1000

# print(f'{metros} metros equivalem a {cm} centimetros, ou {mm} milimetros')

# -------------------------------------------------------------------------------------------------------------

# 5 - FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA 

# numero = int(input('Digite um número: '))

# x1 = numero * 1
# x2 = numero * 2
# x3 = numero * 3
# x4 = numero * 4
# x5 = numero * 5
# x6 = numero * 6
# x7 = numero * 7
# x8 = numero * 8
# x9 = numero * 9
# x10 = numero * 10

# print(f'{numero} x 1 = {x1}\n{numero} x 2 = {x2}\n{numero} x 3 = {x3}\n{numero} x 4 = {x4}\n{numero} x 5 = {x5}\n{numero} x 6 = {x6}\n{numero} x 7 = {x7}\n{numero} x 8 = {x8}\n{numero} x 9 = {x9}\n{numero} x 10 = {x10}\n')

# -------------------------------------------------------------------------------------------------------------

# 6 - CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR 

# dinheiro = float(input('Quantidade de dinheiro na carteira: '))
# dolar = 3.27

# podeComprar = dinheiro / dolar

# print(f'ele pode comprar {podeComprar:.2f} dolares')

# -------------------------------------------------------------------------------------------------------------

# 7 - FAÇA UM PROGRAMA QUE LEIA A LARGURA EA ALTURA DE UMA PAREDE EM METROS. CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA. SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2 METROS QUADRADOS. 

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))

area = largura * altura

qtdTinta = area / 2

print(f'Para pintar uma parede de {area:.0f} metros quadrados é necessário {qtdTinta:.0f} litros de tinta!')





