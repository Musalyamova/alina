#1 задание
n = int(input())
max_a = int(input())
max_n = 1

min_n = 1
min_a = max_a

for i in range(2,n+1):
    a = int(input())
    if a >= max_a:
        max_a = a
        max_n = i
    if a < min_a:
        min_a = a
        min_n = i

print('номер максимального из чисел: ',max_n)
print('номер миниимального из чисел: ',min_n)

#2 задание
n = int(input())
max_sum = []
min_pr = []
for i in range(1,n+1):
    a = int(input('1: '))
    b = int(input('2: '))
    max_sum.append(a+b)
    min_pr.append(a*b)
    if i != n:
        print('следующая пара')
print(max(max_sum), min(min_pr))

#3 задание

n = int(input())
max_sum = -100000000
min_sum = 1000000000
a = int(input())
for i in range(1,n+1):
    b = int(input())
    if (a+b)>=max_sum:
        max_sum = (a+b)
        a = b
    elif (a+b)<=min_sum:
        min_sum = (a+b)
        a = b
print(max_sum, min_sum)

#4 задание
n = input('введите название города: ')
if len(n) % 2 == 0:
    print('четно')
else:
    print('нечетно')


#5 задание
fam1 = input()
fam2 = input()
if len(fam1) > len(fam2):
    print(fam1)
else:
    print(fam2)

#6 задание
s = str(input())
if s[0] == s[-1]:
    print('слово начинается на одну и ту же букву')
else:
    print('слово начинается на одну и ту же букву')

#7 задание
a = str(input())
b = str(input())

if a[0] == b[-1]:
    print('высказывание верно')
else:
    print('высказывание неверно')

#8 задание
s = ''
a = str(input())
s +=str(a[1])
s += str(a[3])
print(s)

#9 задание
s = ''
a = str(input())
s +=str(a[1:4])
print(s)

#10 задание
s = ''

a = (input())
m = int(input())
n = int(input())

s +=str(a[m:n+1])
print(s)

#11 задание
s = 'яблоко'
print(s[1:5])
print(s[3:6])

#12 задание

summa = 0
while True:
    a = int(input())
    if a > 0 and a % 2 == 0:
        summa += a
    if a == 0:
        break
print(summa)

#13 задание

k = int(input())
n = 0
while True:
    n += 1
    a = int(input())
    if a > k:
        print(n)
        break
    if a == 0:
        break