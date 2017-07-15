#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=120
# A: http://www.hacker.org/challenge/chal.php?answer=72181773758939.7&id=120&go=Submit

import decimal
import BiggerFib

def main():
    decimal.getcontext().Emax = 99999999999999
    
    print('{0:.1f}'.format(BiggerFib.fib(150000000000000).ln()))

if __name__ == '__main__':
    main()
