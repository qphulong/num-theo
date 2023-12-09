# find x that x^2 = -1 mod p
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

# example
print(find_square_root_of_minus_one(34214640152883941))
# answer is 30930008016359379 tested