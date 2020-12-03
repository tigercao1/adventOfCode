myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()
content_list = content_list[:len(content_list)-1]

def get_num_trees(bigmap):
    x, y = 0, 0
    num_trees = 0
    while y < len(bigmap) - 1:
        if x + 3 > len(bigmap[0]) - 1:
            minus = len(bigmap[0]) - 1 - x
            x = 3 - minus - 1
        else:
            x += 3
        y += 1
        if bigmap[y][x] == "#":
            num_trees += 1
    return num_trees

print(get_num_trees(content_list))

