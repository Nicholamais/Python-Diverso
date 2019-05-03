l = int(input('Número de elementos da lista\n'))
v = []
c = []
d = []

#Criando a lista
for k in range(0, l):
    print('Digite o ', k+1, 'ºtermo.\n')
    a = (input())
    v.append(a)

print('Sua lista é:',v)
print('com ', l, 'elementos')

p = (input('Digite o número a ser removido de toda a lista.\n'))

#Criando a lista sem os elementos p
for x in range(0, l):
    if v[x] != p:
        c.append(v[x])
    else:
        d.append(v[x])
print('Sua nova lista é: ',c)
print('Com ', len(c), ' elementos e', len(d), 'elementos removidos.')