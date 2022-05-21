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
#soma dos m números
sm = 0
for i in listm:
    sm += i
#soma dos digitos de sm originando sd
sd = 0
while (sm != 0):
    div = sm % 10
    sm = sm // 10
    sd = sd + div
#determinador de método
#observação: prestar atenção na nomenclatura, pois cada variavel pertence a um emtodo especifico
sn = 0
contb = 0
seq_a2 = 1
seq_b = 0
seq_a = 0
seq_1b = 1
seq_2b = 1
if sd % 2 == 0:
    print('método A')
    bubble_sort(listn)
    for i in listn:
        sn += listn[seq_a] * seq_a2

        seq_a += 1
        seq_a2 += 1
else:
    print('método B')
    for i in listn:
        listn[seq_b] += seq_1b
        seq_1b += seq_2b
        seq_2b +=1
        seq_b += 1
    for k in listn:
        sn += listn[contb] % 10 + (listn[contb] // 10)%10
        contb += 1
#determinar dia e mês, atenção com o resto 0, pois para dia vale 31 e para mês vale dezembro
invdia = sn % 31
if invdia == 0:
    invdia = 31
invmes = sn % 12
listmes=['dezembro','janeiro', 'fevereiro', 'março', 'abril','maio','junho','julho','agosto','setembro','outubro','novembro']
mes = listmes[invmes]
if mes == 'fevereiro' and invdia > 28:
    print('código corrompido!')
elif mes == 'abril' or mes == 'junho' or mes == 'setembro' or mes == 'novembro' and invdia > 30:
    print('código corrompido!')
else:
    invasao = print(f'Invasão: {invdia} de {mes}')

