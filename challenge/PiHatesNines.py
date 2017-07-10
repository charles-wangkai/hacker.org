#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=93
# A: http://www.hacker.org/challenge/chal.php?answer=8606570661584407016735064684551083448304103407143306886135064816123133500844233624141744252203847162068581577800344074422408&id=93&go=Submit

# Long run program, so would be better to run on a VPS like Amazon EC2. (Elapsed time: 1:04:46.278042)

# https://en.wikipedia.org/wiki/John_Machin

import datetime
import decimal

def arctan_for_inverse(denominator, error):
    result = decimal.Decimal('1') / decimal.Decimal(denominator)
    
    factor = denominator * denominator
    divisor = 1
    term = result
    while term > error:
        divisor += 2
        term /= factor
        result -= term / divisor
        
        divisor += 2
        term /= factor
        result += term / divisor
    
    return result

def find_longest_non_nine_sequence(digits):
    result = ''
    start_index = 0
    for i in range(len(digits) + 1):
        if i == len(digits) or digits[i] == '9':
            sequence = digits[start_index:i]
            if len(sequence) > len(result):
                result = sequence
            start_index = i + 1
    return result

def compute_pi_digits(precision):
    decimal.getcontext().prec = precision + 5
    error = decimal.Decimal('1E{exponent}'.format(exponent=-(precision + 5)))
    
    pi = 4 * (4 * arctan_for_inverse(5, error) - arctan_for_inverse(239, error))
    
    s = str(pi)
    return s[:1] + s[2:precision + 1]

def solve():
    precision = 1000000
    pi_digits = compute_pi_digits(precision)
    print(find_longest_non_nine_sequence(pi_digits))
    
def main():
    begin_time = datetime.datetime.now()
    solve()
    end_time = datetime.datetime.now()
    print('Elapsed time: {elapsed_time}'.format(elapsed_time=str(end_time - begin_time)))

if __name__ == '__main__':
    main()
