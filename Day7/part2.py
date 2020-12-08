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
        temp = dict(reversed(i.split(" ", 1)) for i in temp)
        bag_map[a[0]] = temp

    return bag_map

def find(bagmap, curr):
    v = bagmap[curr]

    if "other" in v:
        return 0
    
    curr_count = 0
    for key, count in bagmap[curr].items():
        curr_count += int(count) + int(count) * find(bagmap, key)
    
    return curr_count

def count_bags(bagmap):
    return find(bagmap, "shiny gold")

'''
from gold, get children, get count use formula
'''


print(count_bags(process_arr(content_list)))
