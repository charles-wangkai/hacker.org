#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=147
# A: http://www.hacker.org/challenge/chal.php?answer=49122557320&id=147&go=Submit

def main():
    primes = [True] * 1000000000
    
    result = 0
    prime_num = 0
    for i in range(2, len(primes)):
        if primes[i]:
            prime_num += 1
            
            if 49999951 <= prime_num <= 50000000:
                result += i
            
            for j in range(i * i, len(primes), i):
                primes[j] = False
    
    print(result)

if __name__ == '__main__':
    main()
