This is a graph DSA problem using DFS approach : microsoft level
Board: find biggest integer forming from 4 neighbour

def solution(Board):
    # Implement your solution here
    rows = len(Board)
    cols = len(Board[0])
    biggest_int = 0
 
    def dfs_traversal(row, col, path, digit):
        nonlocal biggest_int
        if len(path) == 4:
            biggest_int = max(biggest_int, int(digit))
            return
        for dir_row, dir_col in [(0,1), (1,0), (0,-1),(-1,0)]:
            next_row = row+dir_row
            next_col = col+dir_col
            if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in path:
               dfs_traversal(next_row, next_col, path | {(next_row, next_col)}, digit + str(Board[next_row][next_col]))
 
    # Traversal
    for row in range(rows):
        for col in range(cols):
            dfs_traversal(row, col, {(row, col)}, str(Board[row][col]))
 
    return biggest_int
