#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=19
# A: http://www.hacker.org/challenge/chal.php?answer=4092&id=19&go=Submit

def main():
    BEGIN, END = 10, 17
    
    fibonacci_numbers = [1, 1]
    while len(fibonacci_numbers) < END:
        fibonacci_numbers.append(fibonacci_numbers[-2] + fibonacci_numbers[-1])
    print(sum(fibonacci_numbers[BEGIN - 1:]))

if __name__ == '__main__':
    main()
