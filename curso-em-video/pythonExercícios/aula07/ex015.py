# 11 - ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60POR DIA E R$0.15 POR KM RODADO. 

dias = int(input('Quantos dias alugado: '))
km = float(input('Quantos km rodados: '))

pagar = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${pagar:.2f}')
