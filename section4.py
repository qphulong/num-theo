def repeated_squaring_to_calculate_pow(a,e):
    result = 1

    # Convert the exponent to its binary representation
    binary_exponent = bin(e)[2:]

    for bit in binary_exponent:
        result = result * result

        if bit == "1":
            result = result * a
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
    if repeated_squaring_to_calculate_pow(a,(p - 1) // 2 ) % p == 1:
        return 1
    else:
        return -1

def jacobi_symbol(a, n):
    result = 1
    while True:
        a = a % n
        if a == 0:
            if n == 1:
                return result
            else:
                return 0
        
        a0 = 0 
        h = 0
        while a0 % 2 == 0:
            a0 = a // repeated_squaring_to_calculate_pow(2, h)
            h += 1
        h -= 1
        
        if h % 2 != 0 and n % 8 not in (1,7):
            result *= -1
        if a0 % 4 != 1 and n % 4 == 3:
            result *= -1

        a, n = n, a0
    
    return result


def quandratic_residuosity_test(a, n):
    if jacobi_symbol(a,n) == -1:
        return False
    factors = factorize(n)

    for factor, order in factors:
        if order % 2 == 0 and legendre_symbol(a, factor) == -1:
            return False
    return True

def QR_problem(n, B):
    factors = factorize(n)

    for factor, order in factors:
        if legendre_symbol(B, factors) == -1:
            return False
        
    return True


        


