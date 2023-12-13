# EXERCISE 1
# CONGRUENCE, REPEATED SQUARING, EULER THEOREM
from section4 import factorize

def unit_function(n: int) -> int:
    return 1

def I(n: int) -> int:
    return 1 if n == 1 else 0

def summation_over_divisor(n: int) -> int:
    # Initialize the sum of divisors
    divisors_sum = 0

    # Iterate through numbers from 1 to sqrt(n) (inclusive)
    for i in range(1, int(n**0.5) + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            divisors_sum += i

            # If i is not the square root of n, add the corresponding factor
            if i != n // i:
                divisors_sum += n // i

    return divisors_sum

def mobius(n: int) -> int:
    factors = factorize(n)
    count = 0
    for factor, order in factors:
        if order > 1:
            return 0
        count += 1
    return 1 if count % 2 == 0 else -1
    
def modularInverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
print (modularInverse(37*37,2023*2023)) 
def CONGRUENCE(a,b,m):
    if (a-b)%m==0:
        return True
    else:
        return False
def check(b,m):
    for i in range(1,m):
        if CONGRUENCE(i*i,b,m):
            return i
    return True
