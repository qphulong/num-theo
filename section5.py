from section2 import extended_euclidean

from math import sqrt

def modularSquareRoot(a, p):
    for i in range(1, p):
        if i * i % p == a:
            return i
    return None

#print(modularSquareRoot(448, 2019**2))

def chinesesRemainder(n, a):
    sum = 0
    prod = 1
    for i in range(len(n)):
        prod *= n[i]
    
    for i in range(len(n)):
        p = prod // n[i]
        sum += a[i] * modularInverse(p, n[i]) * p
    
    return sum % prod

def modularInverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

print(pow(9, 9**9, 1001))

def noneffectiveFermat(p):
    for i in range (1, int(sqrt(p))):
        q = sqrt(p - pow(i, 2))
        if q == int(q):
            return i, int(q)
    return None

print(noneffectiveFermat(252497801))
a=[41,152,263]
n=[23,81,127]
print(chinesesRemainder(a,n))