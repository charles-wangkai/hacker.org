#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=258
# A: http://www.hacker.org/challenge/chal.php?answer=58&id=258&go=Submit

def main():
    def display():
        print('After %d days, the population is %d.' % (day, population))
    
    n1, n2, n3, n4 = 0, 1, 0, 0
    
    day = 1
    while True:
        n1, n2, n3, n4 = n1 + n2, n1, n2, n3
        
        population = n1 + n2 + n3 + n4
        if day == 8:
            display()
        if population >= 1000000000000:
            display()
            break
        
        day += 1

if __name__ == '__main__':
    main()
