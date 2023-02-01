# 3 - DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO. CALCULE E MOSTRE SUA MÉDIA

nomeAluno = input('Nome do aluno: ')
quantidadeNotas = int(input('Digite a quantidade de notas: '))

humanas = float(input('Nota humanas: '))
exatas = float(input('Nota exatas: '))

media = (humanas + exatas) / quantidadeNotas

print(f'A media do(a) {nomeAluno} é {media:.1f}')
