#%%

# Parte 1
import re
res = 0

with open('input.txt', 'r', encoding="utf-8") as f:    
    for line in f:
        multipliers = re.findall(r"mul\(\d+,\d+\)", line)
        for mul in multipliers:
            mults = re.search(r"(\d+),(\d+)", mul)
            res += int(mults.group(1)) * int(mults.group(2))

print(res)
# %%
# Parte 2

res_2 = 0

with open('input.txt', 'r', encoding="utf-8") as f:   
    do = True 
    for line in f:
        instruction = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

        for inst in instruction:
            if(re.search(r"don't\(\)",inst)):
                do = False
            elif(re.search(r"do\(\)",inst)):
                do = True
            elif(do):
                mults = re.search(r"(\d+),(\d+)", inst)
                res_2 += int(mults.group(1)) * int(mults.group(2))  

print(res_2)       
