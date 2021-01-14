myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

limit = int(content_list[0])
data = list(int(item) for item in content_list[1].split(","))

import collections

class LRU_idx:
    def __init__(self, l=[]):
        self.storage = collections.OrderedDict()
        for i, item in enumerate(l):
            self.add(item, i+1)

    def add(self, num, idx):
        if num in self.storage:
            self.storage[num] = (idx, max(self.storage[num]))
            self.storage.move_to_end(num)
        else:
            self.storage[num] = (idx, -1)

    def get(self, key):
        return self.storage[key]

    def get_last_key(self):
        return next(reversed(self.storage))

    def is_empty(self):
        return len(self.storage) == 0

def find_number(condition, puz_input):

    storage = LRU_idx(puz_input)

    for i in range(len(puz_input), condition):
        last_key = storage.get_last_key()
        last_item = storage.get(last_key)
        if -1 not in last_item:
            curr_num = abs(last_item[0] - last_item[1])
        else:
            curr_num = 0
        storage.add(curr_num, i+1)
    return storage.get_last_key()

print(find_number(limit, data))

'''

0,3,6

0,3,6,0,3,3,1,0


6:(2,-1)
3:(5,4)
1:(6,-1)
0:(7,3)

if -1 not in orderedmap[-1]:
    curr_num = abs(ordredmap[-1][0] - ordredmap[-1][1])
else:
    curr_num = 0

if curr_num in map:
    move the element to the end, replace the min element with curr idx

'''