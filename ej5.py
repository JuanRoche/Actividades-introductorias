num = 0
list = []
for i in range(11):
    list.append(int(input('ingrese un numero: ')))


for i in list:
    if(i < 0):
        break
    print(i)

