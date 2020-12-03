myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()
content_list = content_list[:len(content_list)-1]

def multiply(arr):
    product = 1
    for a in arr:
        product *= a
    return product

def get_num_trees(bigmap):
    x, y, num_trees = [0 for i in range(5)], [0 for i in range(5)], [0 for i in range(5)]
    moves = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    while sum(y) < 5* (len(bigmap) - 1):
        for i, (xmove, ymove) in enumerate(moves):
            if x[i] + xmove > len(bigmap[0]) - 1:
                x[i] = xmove - (len(bigmap[0]) - 1) % x[i] - 1
            else:
                x[i] += xmove
            if y[i] < len(bigmap) - 1 and y[i] + ymove <= len(bigmap) - 1:
                y[i] += ymove
                if bigmap[y[i]][x[i]] == "#":
                    num_trees[i] += 1
    return multiply(num_trees)


print(get_num_trees(content_list))