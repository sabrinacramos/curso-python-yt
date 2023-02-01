# 2 - CRIE UM ALGORITIMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print(f'O número digitado foi {n}, o drobro dele é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz:.2f}.')
