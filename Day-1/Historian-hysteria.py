#%%
# PARTE 1

# input:
left_list = []
right_list = []

with open('input-1.txt', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip().split('   ')
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

# solucion:
# ordeno ascendentemente
sorted_left = sorted(left_list)
sorted_right = sorted(right_list)

res = 0
for i in range(len(sorted_left)): # ambas listas tienen el mismo size
    res += abs(sorted_left[i] - sorted_right[i])

print(res)

#%%
# PARTE 2

similarity_score = 0
for elem in left_list:
    appearances = right_list.count(elem)
    similarity_score += elem*appearances

print(similarity_score)