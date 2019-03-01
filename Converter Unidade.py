ui = str(input('Escolha a unidade inicial :km,hm,dam,m,dm,cm,mm. \n'))

x= float(input('Valor da distância:\n'))

if ui=='km':
    print(x, ui, '=' ,x * 1, 'km')
    print(x, ui, '=', x * 10, "hm")
    print(x, ui, '=', x * 100, 'dam')
    print(x, ui, '=', x * 1000, 'm')
    print(x, ui, '=', x * 10000, 'dm')
    print(x, ui, '=', x * 100000, 'cm')
    print(x, ui, '=', x * 1000000, 'mm')

if ui=='hm':
    print(x, ui, '=' ,x / 10, 'km')
    print(x, ui, '=', x * 1, 'hm')
    print(x, ui, '=', x * 10, 'dam')
    print(x, ui, '=', x * 100, 'm')
    print(x, ui, '=', x * 1000, 'dm')
    print(x, ui, '=', x * 10000, 'cm')
    print(x, ui, '=', x * 100000, 'mm')

if ui=='dam':
    print(x, ui, '=' ,x / 100,'km')
    print(x, ui, '=', x / 10, "hm")
    print(x, ui, '=', x * 1, 'dam')
    print(x, ui, '=', x * 10, 'm')
    print(x, ui, '=', x * 100, 'dm')
    print(x, ui, '=', x * 1000, 'cm')
    print(x, ui, '=', x * 10000, 'mm')

if ui=='m':
    print(x, ui, '=' ,x / 1000,'km')
    print(x, ui, '=', x / 100, "hm")
    print(x, ui, '=', x * 10, 'dam')
    print(x, ui, '=', x * 1, 'm')
    print(x, ui, '=', x * 10, 'dm')
    print(x, ui, '=', x * 100, 'cm')
    print(x, ui, '=', x * 1000, 'mm')

if ui=='dm':
    print(x, ui, '=' ,x / 10000,'km')
    print(x, ui, '=', x / 1000, "hm")
    print(x, ui, '=', x * 100, 'dam')
    print(x, ui, '=', x * 10, 'm')
    print(x, ui, '=', x * 1, 'dm')
    print(x, ui, '=', x * 10, 'cm')
    print(x, ui, '=', x * 100, 'mm')

if ui=='cm':
    print(x, ui, '=' ,x / 100000,'km')
    print(x, ui, '=', x / 10000, "hm")
    print(x, ui, '=', x / 1000, 'dam')
    print(x, ui, '=', x / 100, 'm')
    print(x, ui, '=', x / 10, 'dm')
    print(x, ui, '=', x * 1, 'cm')
    print(x, ui, '=', x * 10000, 'mm')

if ui=='mm':
    print(x, ui, '=' ,x / 10000000,'km')
    print(x, ui, '=', x / 1000000, "hm")
    print(x, ui, '=', x / 100000, 'dam')
    print(x, ui, '=', x / 10000, 'm')
    print(x, ui, '=', x / 1000, 'dm')
    print(x, ui, '=', x / 10, 'cm')
    print(x, ui, '=', x * 1, 'mm')



