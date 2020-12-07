myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

import collections
'''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

for each color run bfs, if gold, +1, if no other, skip


'''

def process_arr(arr):
    bag_map = collections.OrderedDict()
    for line in arr:
        a = line.split(" bags contain ")
        temp = a[1].replace(" bags, ", ",")
        temp = temp.replace(" bag, ", ",")
        temp = temp.replace(" bags.", "")
        temp = temp.replace(" bag.", "")
        temp = temp.split(",")
        for i, e in enumerate(temp):
            if e != "no other":
                temp[i] = e[2:]
        bag_map[a[0]] = temp
    return bag_map

def find(bagmap):
    count = 0
    for key, i in bagmap.items():
        if key != "shiny gold":
            bigdeck = collections.deque([key])
            while bigdeck:
                curr = bigdeck.popleft()
                if curr == "no other":
                    continue
                if curr == "shiny gold":
                    count += 1
                    break
                bigdeck.extend(bagmap[curr])
    return count




print(find(process_arr(content_list)))
