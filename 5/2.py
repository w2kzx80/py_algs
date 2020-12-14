
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections

ha = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}
hai = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F'
}

c1 = input('Hex1 = ')
c2 = input('Hex2 = ')

h1 = collections.OrderedDict()
h2 = collections.OrderedDict()

for k, v in enumerate(c1[::-1]):
    h1[k] = ha[v]

for k, v in enumerate(c2[::-1]):
    h2[k] = ha[v]

print(h1)
print(h2)

# Сложение
hsum = collections.OrderedDict()
hsum = h1.copy()
for k, v in h2.items():
    if not k in hsum:
        hsum[k] = 0
    hsum[k] += v
    if hsum[k] > 15:
        hsum[k] = hsum[k] - 16
        if not (k+1) in hsum:
            hsum[k+1] = 0
        hsum[k+1] += 1

print("Sum = ",end="")
print([hai[v] for k,v in hsum.items()][::-1])
