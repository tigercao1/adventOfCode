myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

content_list = [x.split(" = ") for x in content_list]

def get_list_of_index(idx, mask):
    list_of_idx = []

    idx_binary = format(idx, '0{}b'.format(len(mask)))

    floating_length = 0
    for c in range(len(mask)):
        if mask[c] == "X":
            floating_length += 1
        if mask[c] != "0":
            idx_binary = idx_binary[:c] + mask[c] + idx_binary[c+1:]

    for i in range(1 << floating_length):
        combination = format(i, '0{}b'.format(floating_length))
        c_in_comb = 0
        temp = idx_binary
        for index, c in enumerate(temp):
            if c == "X":
                temp = temp[:index] + combination[c_in_comb] + temp[index+1:]
                c_in_comb += 1
        list_of_idx.append(int(temp, 2))
    return list_of_idx

def calculate():
    mask = ""
    idx_map = {}
    curridx = 0
    mem = []
    mask_len = 0
    list_of_idx = []
    
    for line in content_list:
        if "mask" in line[0]:
            mask = line[1]
        else:
            idx = int(line[0][4: len(line[0])-1])
            list_of_idx = get_list_of_index(idx, mask).copy()


            for idx in list_of_idx:
                if idx not in idx_map:
                    idx_map[idx] = curridx
                    mem.append(int(line[1]))
                    curridx += 1
                else:
                    mem[idx_map[idx]] = int(line[1])


    return sum(mem)

print(calculate())

def print_01(length):
    for i in range(1 << length):
        print(format(i, 'b'))

'''
3

1000


'''

'''
get mask

convert each number into binary

fill 0 in front

convert index to binary

if mask[i] is X
    record position

101
001

111
001
011

         101
         001
         000
    011       111
    010       110


1000

1000

3

10

000
010
011
001
100
110
111
101


for i in 0,1
    for j in 0,1
        for k in 0,1
            print(i,j,k)




'''