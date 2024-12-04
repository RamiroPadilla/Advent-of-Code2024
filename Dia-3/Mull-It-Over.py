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
