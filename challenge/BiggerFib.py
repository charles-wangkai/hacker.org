#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=118
# A: http://www.hacker.org/challenge/chal.php?answer=72181772.954&id=118&go=Submit

import decimal

def multiply_vector_by_matrix(v, m):
    size = len(v)
    
    result = [0] * size
    for i in range(size):
        for j in range(size):
            result[i] += v[j] * m[j][i]
    return result

def multiply_matrix_by_matrix(m1, m2):
    size = len(m1)
    
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def pow_matrix(base, exponent):
    size = len(base)
    
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        result[i][i] = 1
    
    while exponent:
        if exponent & 1:
            result = multiply_matrix_by_matrix(result, base)
            
        base = multiply_matrix_by_matrix(base, base)
        exponent >>= 1
    return result

def fib(n):
    state = [decimal.Decimal(1.0), decimal.Decimal(1.0)]
    transition = [[decimal.Decimal(0.0), decimal.Decimal(1.0)], [decimal.Decimal(1.0), decimal.Decimal(1.0)]]
    
    return multiply_vector_by_matrix(state, pow_matrix(transition, n - 2))[1]

def main():
    decimal.getcontext().Emax = 99999999
    
    print('{0:.3f}'.format(fib(150000000).ln()))

if __name__ == '__main__':
    main()
