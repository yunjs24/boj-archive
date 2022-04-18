readline = __import__('sys').stdin.readline
board = [list(map(int, readline().split())) for _ in range(9)]
empties = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]
answer = list()

def sol(empty_idx):
    global board, empties, cnt

    if empty_idx == len(empties):

        for r in board:
            print(*r)
        return True

    else:
        x, y = map(int, empties[empty_idx])
        cand = list(range(1,10))
        for i in range(9):
            #row check
            if board[x][i] in cand: cand.remove(board[x][i])
            #col check
            if board[i][y] in cand: cand.remove(board[i][y])

        r_start = x - x%3
        c_start = y - y%3
        for i in range(r_start, r_start+3):
            for j in range(c_start, c_start+3):        
                if board[i][j] in cand:
                    cand.remove(board[i][j])

        for val in cand:
            board[x][y] = val
            if sol(empty_idx+1):
                return True
            board[x][y] = 0

sol(0)