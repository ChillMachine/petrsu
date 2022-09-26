#Ulyanov E.A. 224-ZИС
import math , random

def erfn(limit):
    limit+=200
    listN = [*range(3,limit,2)]
    tempList = [ ]
    for y in listN:
        tempList = []
        for x in listN[listN.index(y)+1:]:
            if x % y == 0: 
                tempList.append(x)
        for j in tempList:
            listN.pop(listN.index(j))               
    return listN[len(listN)//3*2:]

def pqGenerate(pqLimit):
    p, q = random.choice(erfn(pqLimit)), random.choice(erfn(pqLimit))
    while p == q:
        q = random.choice(erfn(pqLimit))
    return p,q

pqLimit = int(input('pqLimit <= 1.000 : '))
while pqLimit > 1000:
    pqLimit = int(input('pqLimit <= 1.000 : '))
M = int(input('M <= 100.000: '))
while M > 100000:
    M = int(input('M <= 100.000: '))

p, q = pqGenerate(pqLimit)
n = p * q
fn = (p - 1) * (q - 1)

e = 3
while math.gcd(fn, e) != 1:
    e += 2

d = 2
while e * d % fn != 1:
    d += 1
print('p = {}, q = {}'.format(p,q))    
print('n = {}, fn = {}'.format(n,fn))
print('e = {}, d = {}'.format(e,d))
result = M ** e % n
C = (result ** d) % n
print(
'''Исходное значение: {}
Зашифровано: {}
Расшифровано: {}
Cовпадение: {}'''.format(M, result, C, C == M))

