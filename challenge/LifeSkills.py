#!/usr/bin/env python2.6

# Q: http://www.hacker.org/challenge/chal.php?id=117
# A: http://www.hacker.org/challenge/chal.php?answer=821%2C319&id=117&go=Submit

# Use Golly, a Game of Life simulator. It can be shown that after 1500 generations, the populations are always 116. So only need to search the first 1500 generations to find the max population.

import golly as g

GENERATION_NUM = 1500

max_population = -1
best_generation = -1

for generation in range(GENERATION_NUM):
    population = int(g.getpop())
    if population > max_population:
        max_population = population
        best_generation = generation
    
    g.step()

g.note('%d,%d' % (best_generation, max_population))