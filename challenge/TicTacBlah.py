#!/usr/bin/env python3

# Q: http://www.hacker.org/challenge/chal.php?id=37
# A: http://www.hacker.org/challenge/chal.php?answer=0.17810761&id=37&go=Submit

SIZE = 3
PIECE_O = 'O'
PIECE_X = 'X'

draw_num = None
all_num = None

def is_win(board, piece):
    return any(all(board[i][j] == piece for j in range(SIZE)) for i in range(SIZE)) \
        or any(all(board[i][j] == piece for i in range(SIZE)) for j in range(SIZE)) \
        or all(board[i][i] == piece for i in range(SIZE)) \
        or all(board[i][SIZE - 1 - i] == piece for i in range(SIZE))

def is_draw(board):
    return all(all(board[i]) for i in range(SIZE))

def search(board, fill_o_or_x):
    global draw_num, all_num
    
    for i in range(SIZE):
        for j in range(SIZE):
            if not board[i][j]:
                board[i][j] = PIECE_O if fill_o_or_x else PIECE_X
                
                if is_win(board, PIECE_O) or is_win(board, PIECE_X):
                    all_num += 1
                elif is_draw(board):
                    draw_num += 1
                    all_num += 1
                else:
                    search(board, not fill_o_or_x)
                
                board[i][j] = None

def main():
    global draw_num, all_num
    
    board = [[None] * SIZE for _ in range(SIZE)]
    board[1][1] = PIECE_O
    
    draw_num = 0
    all_num = 0
    search(board, False)
    
    print('{0:.8f}'.format(draw_num / all_num))

if __name__ == '__main__':
    main()
