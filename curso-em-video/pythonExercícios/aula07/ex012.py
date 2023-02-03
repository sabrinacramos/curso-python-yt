# 8 - FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O SEU NOVO PREÇO, COM 5% DE DESCONTO

preco = float(input('Digite o preço de um produto: R$'))

desconto = preco * 0.95

print(f'Com 5% de desconto o valor do produto que custa R${preco:.2f} muda para R${desconto:.2f}!')
