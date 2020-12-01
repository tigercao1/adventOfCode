myfile = open("inputc1.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

for i in range(len(content_list)):
    content_list[i] = int(content_list[i])

def threeSum():
    target = 2020
    for i, e in enumerate(content_list):
        complement = target - e
        value = twosum(complement, i)
        if value != -1:
            return e * value
    return -1



def twosum(t, idx):
    target = t
    complements = {}
    for i, e in enumerate(content_list):
        if idx != i:
            complement = target - e
            if e not in complements:
                complements[complement] = e
            else:
                return e * complements[e]
    return -1

print(threeSum())