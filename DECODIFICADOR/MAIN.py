def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
                print(lista)
    return lista

#verificador de m
m = int(input('m: '))
while m <= 0 or m >= 6:
    if m >= 6:
        print('precisa ser menor que 6')
        m = int(input('m: '))
    elif m <=0:
        print('precisa ser maior que 0')
        m = int(input('m: '))
#verificador de n
n = int(input('n: '))
while n <= 0 or n >= 11:
    if n <= 0:
        print('precisa ser maior que 0')
        n = int(input('n: '))
    elif n >= 11:
        print('precisa ser menor que 11')
        n = int(input('n: '))

#criador de lista m
listm = []
contadorm = 0
while contadorm < m:
    ml = int(input(f'm{[contadorm]}: '))
    listm.append(ml)
    contadorm += 1
aB