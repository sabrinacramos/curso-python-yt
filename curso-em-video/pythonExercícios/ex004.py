var1 = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(var1))
print('Só tem espaços?', var1.isspace())
print('É numerico?', var1.isnumeric())
print('É alfabético?', var1.isalpha())
print('É alfanumérico?', var1.isalnum())
print('Está em maiúscula?', var1.isupper())
print('Está em minúscula?', var1.islower())
print('Está capitalizada?', var1.istitle())