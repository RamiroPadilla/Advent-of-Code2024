
#%%
# Parte 1
with open('input.txt', 'r', encoding="utf-8") as txt:    
    matriz = [list(linea.strip()) for linea in txt]

rows = len(matriz)
cols = len(matriz[0])
count_xmas = 0

for i in range(rows):
    for j in range(cols):
        if (matriz[i][j] == 'X'):
            if (j + 3 < cols):      # derecha
                word = ''.join([matriz[i][j+k] for k in range(4)])
                if word == 'XMAS':
                    count_xmas += 1
            if (j - 3 >= 0):        # izquierda
                word = ''.join([matriz[i][j-k] for k in range(4)])
                if word == 'XMAS':
                    count_xmas += 1
            if (i + 3 < rows):      # abajo
                word = ''.join(matriz[i+k][j] for k in range(4))
                if word == 'XMAS':
                    count_xmas += 1
            if (i - 3 >= 0):        # arriba
                word = ''.join([matriz[i-k][j] for k in range(4)])
                if word == 'XMAS':
                    count_xmas += 1
            # diagonales
            if (i+3 < rows and j+3 < cols): 
                word = ''.join([matriz[i+k][j+k] for k in range(4)])
                if word == 'XMAS':
                    count_xmas += 1
            if (i+3 < rows and j-3 >= 0): 
                word = ''.join([matriz[i+k][j-k] for k in range(4)])
                if word == 'XMAS':
                    count_xmas += 1
            if (i-3 >= 0 and j+3 < cols): 
                word = ''.join([matriz[i-k][j+k] for k in range(4)])
                if word == 'XMAS':
                    count_xmas += 1
            if (i-3 >= 0 and j-3 >=0): 
                word = ''.join([matriz[i-k][j-k] for k in range(4)])
                if word == 'XMAS':
                    count_xmas += 1

print(count_xmas)
# %%
# Parte 2
with open('input.txt', 'r', encoding="utf-8") as txt:    
    matriz = [list(linea.strip()) for linea in txt]

rows = len(matriz)
cols = len(matriz[0])
count_mas = 0

for i in range(rows):
    for j in range(cols):
        if (matriz[i][j] == 'A'):
            # diagonales
            if (i+1 < rows and j+1 < cols and j-1 >=0 and i-1 >= 0): 
                word = ''.join([matriz[i+k][j+k] for k in range(-1,2)])
                word2 = ''.join([matriz[i+k][j-k] for k in range(-1,2)])
                if ((word == 'MAS' or word =='SAM') and 
                    (word2 == 'MAS' or word2 =='SAM')):
                    count_mas += 1

print(count_mas)