#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=273
# A: http://www.hacker.org/challenge/chal.php?answer=jumpingfactors&id=273&go=Submit

import operator

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def search_primes(base, prime_num):
    primes = []
    n = base
    for _ in range(prime_num):
        while not is_prime(n):
            n += 1
        primes.append(n)
        n += 1
    return primes

def main():
    n = 36484379009457399269217182889395826722660566693989257289404709863891849615322840169192133464099837107563290320068627859223102364122264401785848633686914239718396824942863542362872670850647423969609315959515511402019435615717737240510626468808851903266920099765545245394707
    
    terms = []
    factor = 2
    while n != 1:
        exponent = 0
        while n % factor == 0:
            n //= factor
            exponent += 1
            
        if exponent:
            terms.append((factor, exponent))
        
        factor += 1
    
    terms.sort(key=operator.itemgetter(1))
    factors = list(map(operator.itemgetter(0), terms))
    
    primes = search_primes(min(factors), 26)
    
    print(''.join(map(lambda factor: chr(primes.index(factor) + ord('a')), factors)))

if __name__ == '__main__':
    main()
