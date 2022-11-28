array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(array):
    if array[i][:1] in '+-':
        if array[i][1:].isdigit():
            array[i] = f'{array[i][:1]}{int(array[i][1:]):02d}'
            array.insert(i,'"')
            array.insert(i + 2,'"')
            i += 2
    elif array[i].isdigit():
            array[i] = f'{int(array[i]):02d}'
            array.insert(i,'"')
            array.insert(i + 2,'"')
            i += 2
    else:
        i += 1

print(' '.join(array))




list = ['инженер-конструктор Игорь','главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй','директор аэлита']
for i in list:
    i = i.split()[-1].title()
    print(f'Привет, {i}!')





list = [57.8, 46.51, 97., 9.]
for i in range(len(list)):
    list[i] = str(list[i]).split('.')
    list[i] = str(list[i][0]).rjust(2, '0') + ' рублей ' + str(list[i][1]).ljust(2, '0') + ' копеек '
for i, arg in enumerate(list, start = 1):
    print(f'№ {i} => {arg}', end=', ')

