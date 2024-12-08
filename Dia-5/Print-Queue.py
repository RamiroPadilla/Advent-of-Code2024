
#%%

import re

adj = {}
visited = {}
finished = []

def DFS(v, list_v):
    global visited, finished
    visited[v] = True
    for u in adj.get(v, []):
        if (not visited.get(u, False) and (u in list_v) ):
            DFS(u, list_v)
    finished.append(v)

def topological_sort(list_v):
    global visited, finished
    visited = {v: False for v in list_v}
    finished.clear()

    for vertice in list_v:
        if (not visited[vertice]):
            DFS(vertice, list_v)
    
    finished.reverse()

with open('input-rules.txt', 'r', encoding="utf-8") as txt:
    for line in txt:
        nums = re.search(r"(\d+)\|(\d+)", line)
        u, v = int(nums.group(1)), int(nums.group(2))
        adj.setdefault(u, []).append(v)

def is_subseq(list_update):
    global finished
    i, j = 0, 0
    
    while (i<len(list_update) and j<len(finished)):
        if (list_update[i] == finished[j]):
            i += 1
        j += 1
    
    return i == len(list_update)

def topoSort(list_update):
    global finished
    sorted_list = [x for x in finished if x in list_update]

    return sorted_list

with open('input-updates.txt', 'r', encoding="utf-8") as txt:
    final_correct_sum = 0
    final_incorrect_sum = 0
    for line in txt:
        update = list(map(int, line.split(',')))
        
        # " Because the first update does not include some page numbers, 
        #   the ordering rules involving those missing page numbers are ignored "
        topological_sort(update) 

        if (is_subseq(update)):
            middle_page_number = update[len(update)//2]
            final_correct_sum += middle_page_number
        else:
            sorted_update = topoSort(update)
            middle_page_number = sorted_update[len(sorted_update)//2]
            final_incorrect_sum += middle_page_number

print(final_correct_sum)

print(final_incorrect_sum)
