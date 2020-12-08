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

    acc = 0
    visited = set()
    visited_target = set()
    idx = 0
    modified = False
    for i, op in enumerate(arr_ops):
        if op == "nop":
            arr_ops[i] = "jmp"
            if get_acc(arr_ops, arr_num) == -1:
                arr_ops[i] = "nop"
            else:
                return get_acc(arr_ops, arr_num)
        elif op == "jmp":
            arr_ops[i] = "nop"
            if get_acc(arr_ops, arr_num) == -1:
                arr_ops[i] = "jmp"
            else:
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
            return -1
        visited.add(idx)
    return acc
print(process_arr(content_list))

'''
list of operations
list of numbers

if seen nop, change to jmp and see if it go back, if not continue, if at any point goes back, go back to nop and continue.
if seen jmp, change to nop and continue, if go back, keep jmp

'''