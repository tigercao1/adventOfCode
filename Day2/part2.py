myfile = open('input.txt', 'r')
content = myfile.read()
content = content.strip()
content_list = content.split('\n')
myfile.close()

def count_valid_password(passwords):
    valid = 0
    for i, e in enumerate(passwords):
        curr = e.split(" ")
        limit = curr[0].split("-")
        for i in range(len(limit)):
            limit[i] = int(limit[i])
        target, password, count = curr[1].strip(":"), curr[2], 0
        for j, c in enumerate(password):
            if (j == limit[0] - 1 or j == limit[1] - 1) and c == target:
                count += 1
        if count == 1:
            valid += 1
    return valid

print(count_valid_password(content_list))