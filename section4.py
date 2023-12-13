import math
import sys
from section2 import extended_euclidean

def repeated_squaring_to_calculate_pow(a,e, mod = None):
    result = 1

    # Convert the exponent to its binary representation
    binary_exponent = bin(e)[2:]

    for bit in binary_exponent:
        result = result * result

        if bit == "1":
            result = result * a
        if mod is not None:
            result = result % mod
    return result

def factorize(n):
    factors = []
    divisor = 2

    while n > 1:
        order = 0

        while n % divisor == 0:
            order += 1
            n //= divisor

        if order > 0:
            factors.append((divisor, order)) 

        divisor += 1

        # If the divisor becomes greater than the square root of n,
        # then n itself is a prime number and should be added as a factor
        if divisor * divisor > n and n > 1:
            factors.append((n, 1))
            break

    return factors


def legendre_symbol(a, p):
    if a % p == 0:
        return 0
    if repeated_squaring_to_calculate_pow(a,(p - 1) // 2, p) == 1:
        return 1
    else:
        return -1
    
print(legendre_symbol(873, 673))

def jacobi_symbol(a, n):
    result = 1
    while True:
        a = a % n
        if a == 0:
            if n == 1:
                return result
            else:
                return 0
        
        a0 = a 
        h = 0
        while a0 % 2 == 0:
            a0 //= 2
            h += 1
        
        if h % 2 != 0 and n % 8 not in (1,7):
            result *= -1
        if a0 % 4 != 1 and n % 4 == 3:
            result *= -1

        a, n = n, a0
    
    return result

print (jacobi_symbol(873, 2019))

def quandratic_residuosity_test(a, n):
    if jacobi_symbol(a,n) == -1:
        return False
    factors = factorize(n)

    for factor, order in factors:
        if order % 2 == 1 and legendre_symbol(a, factor) == -1:
            return False
    return True

def QR_problem(n, B):
    factors = factorize(n)

    for factor, order in factors:
        if legendre_symbol(B, factor) == -1:
            return False
        
    return True

# RSA
# define e = 65537
e = 65537

# p, q are very large prime numbers
def gen_pq():
    return 9967, 9973
        
def carmichael(p, q):
    return math.lcm(p - 1, q - 1)


def find_d(lambda_n):
    '''Given e and c = carmichael(p, q), find d such that ed = 1 (mod c)'''
    return extended_euclidean(e, lambda_n)[1] % lambda_n

def RSA():
    p, q = gen_pq()
    n = p * q
    d = find_d(carmichael(p, q))
    return (e, n), d

def encrypt(plain_text, public_key):
    m = int.from_bytes(plain_text.encode(), 'little')
    print(m)
    return pow(m, public_key[0], public_key[1])

def decrypt(cipher_text, public_key, private_key):
    m = pow(cipher_text, private_key, public_key[1])
    print(m)
    return m.to_bytes(math.ceil(m.bit_length() / 8), 'little').decode()

sys.set_int_max_str_digits(0)
# public_key, private_key = RSA()
# print(public_key, private_key)
# cipher_text = encrypt('ế', public_key)
# print(cipher_text)
# plain_text = decrypt(cipher_text, public_key, private_key)
# print(plain_text)

print(jacobi_symbol(1983,2027))
print(legendre_symbol(1983,2027))
print(jacobi_symbol(873,2029))
print(legendre_symbol(873,2029))
print(jacobi_symbol(474993,1003001))
print(legendre_symbol(474993,1003001))

