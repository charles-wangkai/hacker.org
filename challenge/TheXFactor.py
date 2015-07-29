#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=95
# A: http://www.hacker.org/challenge/chal.php?answer=459905301806642105202622615174502491&id=95&go=Submit

import random

def multiply_mod(x, y, modulo):
    return x * y % modulo

def pow_mod(base, exponent, modulo):
    result = 1
    while exponent:
        if exponent % 2:
            result = multiply_mod(result, base, modulo)
        
        base = multiply_mod(base, base, modulo)
        exponent //= 2
    return result

# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def miller_rabin(n):
    K = 100
    
    if n < 2 or n % 2 == 0:
        return False
    if n in [2, 3]:
        return True
    
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    
    for _ in range(K):
        a = random.randrange(2, n - 1)
        x = pow_mod(a, d, n)
        
        if x in [1, n - 1]:
            continue
        
        outer_continue = False
        for __ in range(s - 1):
            x = multiply_mod(x, x, n)
            if x == 1:
                return False
            if x == n - 1:
                outer_continue = True
                break
        if outer_continue:
            continue
        
        return False
    
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
def pollard_rho(n, g):
    ITERATION_LIMIT = 10000
    
    x, y = random.randrange(n), 2
    d = 1
    for _ in range(ITERATION_LIMIT):
        x, y = g(x), g(g(y))
        d = gcd(abs(x - y), n)
        if d != 1:
            break

    return None if d in [1, n] else d

def factorize(n):
    if miller_rabin(n):
        return [n]
    
    while True:
        factor = pollard_rho(n, lambda x: (x * x + 1) % n)
        if factor:
            result = factorize(factor) + factorize(n // factor)
            return result

def main():
    prime_factors = sorted(factorize(7393913335919140050521110339491123405991919445111971))
    print(*prime_factors, sep=' * ')
        
    print(prime_factors[-1])

if __name__ == '__main__':
    main()
