myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n\n")
myfile.close()

def process_str(arr):
    count = 0
    for item in arr:
        temp = item.split("\n")
        temp = ''.join(temp)
        char_set = set()
        for c in temp:
            if c not in char_set:
                char_set.add(c)
        count += len(char_set)
    return count

print(process_str(content_list))