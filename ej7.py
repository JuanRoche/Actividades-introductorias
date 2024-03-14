list = []
for i in range(11):
    list.append(int(input('ingrese un numero')))

cadena = ''

for i in list:
    if(i % 3 == 0):
        continue
    cadena += str(i) + '-'

print(cadena)    