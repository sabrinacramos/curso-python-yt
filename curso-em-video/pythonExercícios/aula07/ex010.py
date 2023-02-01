# 6 - CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR

real = float(input('Quantidade de dinheiro na carteira: R$'))
dolar = real / 3.27

print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
