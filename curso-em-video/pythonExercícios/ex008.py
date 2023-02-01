# 4 - ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

medida = float(input('Digite uma distância em metros: '))

cm = medida * 100
mm = medida * 1000

print(f'{medida} metros equivalem a {cm:.0f} centimetros, ou {mm:.0f} milimetros')
