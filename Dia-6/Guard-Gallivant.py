
#%%
matriz = []
with open('input-map.txt', 'r', encoding="utf-8") as txt:    
    count_row = 0
    for linea in txt:
        row = list(linea.strip())
        matriz.append(row)        

        if ("^" in row):
            start_row = count_row
            start_col = row.index('^')

        count_row += 1

path = set() 
movements = [(-1,0), (0,1), (1,0), (0,-1)]
# 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT

def out_range(n, m, i, j):
    if (i < 0 or i >= n or j < 0 or j >= m):
        return True

    return False

def start_run(M, i, j):
    global path
    n, m = len(M), len(M[0])
    dir = 0

    while (i < n and j < m):
        path.add((i,j))

        tmp_i, tmp_j = i + movements[dir][0], j + movements[dir][1]

        if (out_range(n, m, tmp_i, tmp_j)): #
            break

        while (M[tmp_i][tmp_j] == '#'):
            dir = (dir + 1) % 4 # mod 
            tmp_i, tmp_j = i + movements[dir][0], j + movements[dir][1]
        

        i, j = tmp_i, tmp_j    
    return len(path)

# %%
start_run(matriz, start_row, start_col)

