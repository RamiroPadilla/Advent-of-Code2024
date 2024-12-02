#%%

count_unsafe = 0
total_lines = 0

with open('input.txt', 'r', encoding="utf-8") as f:
    for line in f:
        line = list(map(int, line.strip().split()))

        if (line[0] < line[1]):
            for i in range(len(line) - 1):            
                if ( abs(line[i] - line[i+1]) > 3 or line[i] >= line[i+1]):
                    count_unsafe += 1
                    break
        else:
            for i in range(len(line) - 1):            
                if ( abs(line[i] - line[i+1]) > 3 or line[i] <= line[i+1]):
                    count_unsafe += 1
                    break   

        total_lines += 1

print(total_lines - count_unsafe)
# %%

# Parte dos
count_safe = 0

def is_safe(line):
    safe = True
    elem = -1
    if (line[0] < line[1]):
        for i in range(len(line) - 1):            
            if ( abs(line[i] - line[i+1]) > 3 or line[i] >= line[i+1]):
                safe = False
                elem = i
                break
    else:
        for i in range(len(line) - 1):            
            if ( abs(line[i] - line[i+1]) > 3 or line[i] <= line[i+1]):
                safe = False
                elem = i
                break  

    return safe, elem


with open('input.txt', 'r', encoding="utf-8") as f:
    for line in f:
        line = list(map(int, line.strip().split()))
        n = len(line)

        safe, id_elem = is_safe(line)

        if (safe):
            count_safe +=1
        else:
            line_tmp = line[:id_elem] + line[id_elem+1:]
            if( is_safe(line_tmp)[0] ) :
                count_safe +=1
            else: 
                if (id_elem > 0 ):
                    line_tmp = line[:id_elem-1] + line[id_elem:]
                    if( is_safe(line_tmp)[0] ) :
                        count_safe +=1

                if (id_elem < n-1):
                    line_tmp = line[:id_elem+1] + line[id_elem+2:]
                    if( is_safe(line_tmp)[0] ) :
                        count_safe +=1

print(count_safe)