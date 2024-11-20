a = 34
b = 45
if a < b:
    a = 0
    print(a,b)
else:
    print(a,b)

a = [-1,3,-5]
for i in a:
    if i >= 0:
        print(i ** 2, end = ' ')

a = int(input())
a = str(a)
sum = 0
for i in a:
    sum += int(i)
print(sum)

a = 1
b = 4
c = 2
s = [a,b,c]
for i in s:
    if 1<i<3:
        print(i, end = ' ')

k = 1
b = int(input())
print(b)
while k == 1:
    a = int(input())
    if b <= a:
        b = a
    else:
        k = 0
        break
print(a)
