def f21(x):
    list2 = ['genie', 'slash', 'wisp']
    list3 = [1988, 1997]
    list1 = ['bison', 'sqf', 'xs']
    if list2.index(x[2]) == 0:
        y = [list2.index(x[2]), list3.index(x[3]), list1.index(x[1])]
    else:
        y = [list2.index(x[2]), list1.index(x[1]), list3.index(x[3])]
    d = {'000': 0, '001': 1, '002': 2, '01': 3, '100': 4, '101': 5, '11': 6, '12': 7, '20': 8, '21': 9, '22': 10}
    test = ''.join(str(e) for e in y)[:2]
    if test in d:
        return d[test]
    else:
        return d[''.join(str(e) for e in y)]


def f22(x):
    d = (x & 0xFE000000)
    c = (x & 0x01F80000) >> 19
    b = (x & 0x0007FFF8) << 6
    a = (x & 0x00000007) << 6
    return hex(a + b + c + d)


def f23(table):
    s = set()
    l = []
    for row in table:
        s.add(tuple(row))
    s.discard((None, None, None, None))
    for row in s:
        l.append(list(row))
    for row in l:
        row[0] = row[0].split(' ')[2] + ' ' + row[0].split(' ')[0]
        if row[1] == 'Y':
            row[1] = 'Выполнено'
        else:
            row[1] = 'Не выполнено'
        row[2] = '{:.0%}'.format(row[2])
    l.sort()
    return l


print(f21([1968, 'xs', 'genie', 1988]))
print(f23([['Валерий Ц. Забачянц', 'Y', 0.233],
     [None, None, None, None],
     ['Павел Б. Цивко', 'Y', 0.258],
     ['Дамир Д. Руцорли', 'N', 0.988],
     ['Валерий Ц. Забачянц', 'Y', 0.233]]))
print(f22(0x79e422a2))
