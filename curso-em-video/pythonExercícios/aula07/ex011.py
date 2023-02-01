# 7 - FAÇA UM PROGRAMA QUE LEIA A LARGURA EA ALTURA DE UMA PAREDE EM METROS. CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA. SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2 METROS QUADRADOS.

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

qtdTinta = area / 2

print(f'Para pintar uma parede de dimensão de {largura}x{altura} em uma área de {area:.2f}m² é necessário {qtdTinta:.0f}l de tinta!')
