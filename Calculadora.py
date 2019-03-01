op = int(input('1 para somar, 2 para subtrair, 3 para multiplicar, 4 para dividir e 5 para todas as operações. \n'))


n1 = float(input('Primeiro número: \n'))
n2 = float(input('Segundo número: \n'))

if op==1:
    print(n1, '+' ,n2, '=', n1+n2)

if op==2:
    print(n1, '-', n2, '=', n1 - n2)

if op==3:
    print(n1, '*', n2, '=', n1 * n2)

if op==4:
    if n2==0:
        print('Não é possível dividir por zero. Valor inderteminado')
    else:
         print(n1, '/', n2, '=', n1 / n2)
if op==5:
    print(n1, '+', n2, '=', n1 + n2)
    print(n1, '-', n2, '=', n1 - n2)
    print(n1, '*', n2, '=', n1 * n2)
    if n2 == 0:
        print(n1,'/', n2, '='' Não é possível dividir por zero. Valor inderteminado')
    else:
        print(n1, '/', n2, '=', n1 / n2)

