myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n\n")
myfile.close()

def process_str(arr):
    count = 0
    for item in arr:
        temp = item.split("\n")
        temp.sort(key=lambda x: len(x))
        a = 0
        for c in temp[0]:
            not_in = False
            for i in range (1, len(temp)):
                if c not in temp[i]:
                    not_in = True
                    break
            if not not_in:
                a += 1
        count += a
    return count

print(process_str(content_list))