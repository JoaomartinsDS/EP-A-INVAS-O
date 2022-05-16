def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
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
#criador de lista n
listn = []
contadorn = 0
while contadorn < n:
    nl = int(input(f'n{[contadorn]}: '))
    listn.append(nl)
    contadorn += 1
sm = 0
for i in listm:
    sm += i
sd = 0
while (sm != 0):
    div = sm % 10
    sm = sm // 10
    sd = sd + div
sn = 0
mult = 0
seq_metodoa = 1
complementar = 0
seq_2 = 0
seq_1b = 1
seq_2b = 1
if sd % 2 == 0:
    print('método A')
    bubble_sort(listn)
    for i in listn:
        sn += listn[seq_2] * seq_metodoa

        seq_2 += 1
        seq_metodoa += 1
else:
    print('método B')
    for i in listn:
        listn[complementar] += seq_1b
        seq_1b += seq_2b
        seq_2b +=1
        complementar += 1
    for k in listn:
        sn += listn[mult] % 10 + (listn[mult] // 10)%10
        mult += 1
invdia = sn % 31
if invdia == 0:
    invdia = 31
invmes = sn % 12
listmes=['dezembro','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro']
mes = listmes[invmes]
if mes == 'fevereiro' and invdia > 28:
    print('código corrompido!')
else:
    invasao = print(f'Invasão: {invdia} de {mes}')

