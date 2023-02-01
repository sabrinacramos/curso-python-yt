# 9 - FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO COM 15% DE AUMENTO
salario = float(input('Digite o salario do funcionário: R$ '))

aumento = salario + (salario * 15 / 100)

print(f'Com o aumento de 15% o salario foi de R${salario:.2f} para R${aumento:.2f}')
