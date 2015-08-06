#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=148
# A: http://www.hacker.org/challenge/chal.php?answer=Beelzebub&id=148&go=Submit

import random
import re
import urllib.request
import hacker_org_util

LEVEL_UP = 4

def is_won(source):
    return 'You are triumphant' in source

def is_died(source):
    return 'You have died' in source

def is_idle(source):
    return 'Move:' in source

def has_treasure(source):
    return 'Pick up treasure:' in source

def find_available_moves(game_id, source):
    return re.findall(r'(?<=<a href={game_id}.php\?m=).*?(?=>)'.format(game_id=game_id), source)

def find_available_potions(game_id, source):
    return re.findall(r'(?<=<a href={game_id}.php\?potion=).*?(?=>)'.format(game_id=game_id), source)

def find_my_values(source):
    i = re.compile(r'\d+').finditer(source, re.search(r'<th>weapon</th>', source).end() + 1)
    my_level = int(next(i).group())
    hit_points = int(next(i).group())
    return my_level, hit_points
    
def find_beast_name(source):
    match = re.search(r'(\w+) stands before you.', source)
    return match.group(1) if match else None

def find_dungeon_level(source):
    return int(re.search(r'<h2>Dungeon Level (\d+)</h2>', source).group(1))

def play(game_id):
    base_url = 'http://www.hacker.org/challenge/misc/d/{game_id}.php'.format(game_id=game_id)
    url = base_url
    died_num = 0
    prev_hit_points = None
    max_damage = 0
    beast_name = None
    
    while True:
        source = urllib.request.urlopen(hacker_org_util.add_username_password_to_url(url)).read().decode()
        print('died_num:', died_num)
        print(source)
        
        if not beast_name:
            beast_name = find_beast_name(source)
        
        if is_won(source):
            break
        elif is_died(source):
            url = base_url
            died_num += 1
        else:
            my_level, hit_points = find_my_values(source)
            
            if is_idle(source):
                prev_hit_points = None
                max_damage = 0
                
                if has_treasure(source):
                    parameters = 'tres=1'
                else:
                    available_moves = find_available_moves(game_id, source)
                    
                    if 'd' in available_moves:
                        dungeon_level = find_dungeon_level(source)
                        if my_level < dungeon_level + LEVEL_UP:
                            available_moves.remove('d')
                    
                    if 'd' in available_moves:
                        move = 'd'
                    else:
                        move = random.choice(available_moves)
                    parameters = 'm={move}'.format(move=move)
            else:
                if prev_hit_points:
                    max_damage = max(max_damage, prev_hit_points - hit_points)
                    
                available_potions = find_available_potions(game_id, source)
                if available_potions and hit_points <= max_damage:
                    potion = random.choice(available_potions)
                    parameters = 'potion={potion}'.format(potion=potion)
                else:
                    parameters = 'attack=1'
                    
                prev_hit_points = hit_points
            
            print(parameters)
            url = hacker_org_util.add_username_password_to_url('{base_url}?{parameters}'.format(base_url=base_url, parameters=parameters))
    
    print(beast_name)

def main():
    play('index')

if __name__ == '__main__':
    main()
