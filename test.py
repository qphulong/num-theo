#L1
#a
result = pow(2023, 2024, 1000)
print(result)
#c
def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

base = 19
exponent = 19**19
modulus = 1001

result = mod_pow(base, exponent, modulus)
print(f"The remainder of 19^(19^19) when divided by 1001 is: {result}")

#b
base = 20232024
exponent = 20242023
modulus = 12345

result = mod_pow(base, exponent, modulus)
print(f"The remainder of 20232024^20242023 when divided by 12345 is: {result}")

#L2
def find_square_root_of_minus_one(p):
    # If p != 1 (mod 4), return None
    if p % 4 != 1:
        return None
    
    a = 2
    while a < p:
        b = pow(a, (p-1)//4, p)  # Using pow for modular exponentiation
        if (b**2 + 1) % p == 0:
            return b
        a += 1
    return None
#a
print(find_square_root_of_minus_one(2053))
#b
print(find_square_root_of_minus_one(3000017))
#c
print(find_square_root_of_minus_one(1234567913))

#L3
def extended_euclidean(a, b):
    r0, r1 = a,b
    s0, s1= 1,0
    t0, t1= 0,1
    while r1!= 0:
        q = r0 // r1
        r2 = r0 % r1
        r0,s0,t0,r1,s1,t1 = r1,s1,t1,r2,s0-s1*q,t0-t1*q
    d0 = r0
    return d0,s0,t0
#a
print (extended_euclidean(20212019, 909431371))
#b
print (extended_euclidean(12345678, 2345698))
#c
print (extended_euclidean(12345675, 567895))


#L4
#a
print (extended_euclidean(1234567892, 197654321))
#b
def modularInverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
print (modularInverse(37,2023)) 
#c
print (modularInverse(37*37,2023*2023)) 


#L5


#L9
def find_x(base, target, modulus):
    result = 1
    for x in range(modulus):
        if pow(base, x, modulus) == target:
            return x
    return None

base = 37
target = 235
modulus = 2027

result = find_x(base, target, modulus)

if result is not None:
    print(f"The value of x is: {result}")
else:
    print("No solution found.")


