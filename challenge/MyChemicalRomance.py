#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=171
# A: http://www.hacker.org/challenge/chal.php?answer=redsneackers&id=171&go=Submit

# https://en.wikipedia.org/wiki/Periodic_table#/media/File:Periodic_Table_Chart.png

def main():
    number2symbol = {7: 'N', 8: 'O', 10: 'Ne', 16: 'S', 19: 'K', 22: 'Ti', 53: 'I', 68: 'Er', 71: 'Lu', 75: 'Re', 89: 'Ac', 90: 'Th', 99: 'Es', 110: 'Ds'}
    
    s = ['5a', '63', '08', '47', '16', '08', '07', '35', '10', '4b', '6e', '0a', '59', '13', '44', '10']
    print(''.join(map(lambda x: number2symbol[int(x, 16)], s)).lower())

if __name__ == '__main__':
    main()
