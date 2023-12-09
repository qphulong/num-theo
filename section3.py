def eratosthenes(n):
    is_prime = [True] * (n + 1)
    
    # 0 and 1 are not prime numbers
    is_prime[0] = is_prime[1] = False
    
    # Iterate through the numbers 2 to sqrt(n) (inclusive)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as not prime
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # Collect the prime numbers into a list
    primes = [num for num in range(2, n + 1) if is_prime[num]]
    
    return primes

# Example usage:
n = 30
result = eratosthenes(n)
print(result)
