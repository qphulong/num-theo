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
