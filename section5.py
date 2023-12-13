from section2 import extended_euclidean

from math import sqrt

import math

def modularSquareRoot(a, p):
    for i in range(1, p):
        if i * i % p == a:
            return i
    return None

print("modular")
print(modularSquareRoot(1983, 2027))
print(modularSquareRoot(873, 2029))
print(modularSquareRoot(474993, 1003001))

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

#print(pow(9, 9**9, 1001))

def noneffectiveFermat(p):
    for i in range (1, int(sqrt(p))):
        q = sqrt(p - pow(i, 2))
        if q == int(q):
            return i, int(q)
    return None

#print(noneffectiveFermat(252497801))

def float_to_fraction (x, error=0.00001):
    n = int(math.floor(x))
    x -= n
    if x < error:
        return (n, 1)
    elif 1 - error < x:
        return (n+1, 1)

    # The lower fraction is 0/1
    lower_n = 0
    lower_d = 1
    # The upper fraction is 1/1
    upper_n = 1
    upper_d = 1
    while True:
        # The middle fraction is (lower_n + upper_n) / (lower_d + upper_d)
        middle_n = lower_n + upper_n
        middle_d = lower_d + upper_d
        # If x + error < middle
        if middle_d * (x + error) < middle_n:
            # middle is our new upper
            upper_n = middle_n
            upper_d = middle_d
        # Else If middle < x - error
        elif middle_n < (x - error) * middle_d:
            # middle is our new lower
            lower_n = middle_n
            lower_d = middle_d
        # Else middle is our best fraction
        else:
            return (n * middle_d + middle_n, middle_d)
        
print("L6")

print(float_to_fraction(0.372636))
print(float_to_fraction(0.373346671))
print(float_to_fraction(0.2173836482))