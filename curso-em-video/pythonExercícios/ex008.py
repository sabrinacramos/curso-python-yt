# 4 - ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

metros = float(input('Digite o tamanho em métros: '))

cm = metros * 100
mm = metros * 1000

print(f'{metros} metros equivalem a {cm} centimetros, ou {mm} milimetros')
