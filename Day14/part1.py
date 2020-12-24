myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

content_list = [x.split(" = ") for x in content_list]

def calculate():
    mask = ""
    idx_map = {}
    curridx = 0
    mem = []
    mask_len = 0
    for line in content_list:
        if "mask" in line[0]:
            mask = line[1]
            mask_len = len(mask)
        else:
            idx = int(line[0][4: len(line[0])-1])
            binary = format(int(line[1]), '0{}b'.format(mask_len))
            for c in range(len(mask)-1, -1, -1):
                if mask[c] == "1" or mask[c] == "0":
                    binary = binary[:c] + mask[c] + binary[c+1:]
            if idx not in idx_map:
                idx_map[idx] = curridx
                mem.append(int(binary, 2))
                curridx += 1
            else:
                mem[idx_map[idx]] = int(binary, 2)
    return sum(mem)

print(calculate())
            

'''
get mask

convert each number into binary

fill 0 in front



'''