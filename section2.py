import math


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
# print(find_square_root_of_minus_one(34214640152883941))
# answer is 30930008016359379 tested



# extended euclidean algorithm
# given integer a,b >= 0, return s,t,d that 
# d = gcd (a,b) and d = as + bt
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

# print (extended_euclidean(1009, 469))



# given prime p, find r and t such that r^2 + t^2 = p
def find_sum_of_squares(p):
    # find b that b^2 = -1 (mod p)
    b = find_square_root_of_minus_one(p)

    # using euclidean to find r and t
    r0, r1 = p,b
    s0, s1= 1,0
    t0, t1= 0,1
    while r1!= 0:
        q = r0 // r1
        r2 = r0 % r1
        r0,s0,t0,r1,s1,t1 = r1,s1,t1,r2,s0-s1*q,t0-t1*q
        if r0 < math.isqrt(p):
            return r0, t0
        
#print(find_sum_of_squares(686108489463743460363628988309))
