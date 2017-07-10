#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=98
# A: http://www.hacker.org/challenge/chal.php?answer=756130190263&id=98&go=Submit

# Long run program, so would be better to run on a VPS like Amazon EC2. (Elapsed time: about 1 hour)

# Suffix Array:
# https://en.wikipedia.org/wiki/Suffix_array
# http://blog.csdn.net/hackbuteer1/article/details/7968623

import functools
import PiHatesNines

pi_digits = None

def compare_begin_index(i1, i2):
    while True:
        if i1 == len(pi_digits):
            return -1
        elif i2 == len(pi_digits):
            return 1
        elif pi_digits[i1] < pi_digits[i2]:
            return -1
        elif pi_digits[i1] > pi_digits[i2]:
            return 1
        
        i1 += 1
        i2 += 1

def count_common_length(i1, i2):
    common_length = 0
    while i1 != len(pi_digits) and pi_digits[i1] == pi_digits[i2]:
        i1 += 1
        i2 += 1
        common_length += 1
    return common_length

def find_repeated_sequence():
    begin_indices = list(range(len(pi_digits)))
    
    begin_indices.sort(key=functools.cmp_to_key(compare_begin_index))
    
    max_common_length = 0
    result_begin_index = None
    
    for i in range(len(begin_indices) - 1):
        common_length = count_common_length(begin_indices[i], begin_indices[i + 1])
        
        if common_length > max_common_length:
            max_common_length = common_length
            result_begin_index = begin_indices[i]
    
    return pi_digits[result_begin_index : result_begin_index + max_common_length]

def main():
    global pi_digits
    
    pi_digits = PiHatesNines.compute_pi_digits(1000000)

    print(find_repeated_sequence())

if __name__ == '__main__':
    main()
