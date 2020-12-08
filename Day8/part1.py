myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

import collections

def process_arr(arr):
    arr_ops = []
    arr_num = []
    for line in arr:
        sline = line.split()
        arr_ops.append(sline[0])
        if sline[1][0] == "+":
            arr_num.append(int(sline[1][1:]))
        else:
            arr_num.append(int(sline[1]))
    return get_acc(arr_ops, arr_num)

def get_acc(arr_ops, arr_num):
    visited = set()
    acc = 0
    idx = 0
    while idx < len(arr_ops):
        if arr_ops[idx] == "acc":
            acc += arr_num[idx]
        if arr_ops[idx] == "jmp":
            idx += arr_num[idx]
        else:
            idx += 1
        if idx in visited:
            return acc
        visited.add(idx)
    return acc

print(process_arr(content_list))
'''
list of operations
list of numbers



'''