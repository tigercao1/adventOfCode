myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

content_list = list(int(i) for i in content_list)


def two_sum(arr, target):
    complements = {}
    for num in arr:
        complement = target - num
        if num in complements:
            return True
        complements[complement] = num

    return False


def find_invalid(arr):
    for i in range(len(arr)):
        if i > 24:
            is_valid = two_sum(arr[i-25:i], arr[i])
            if not is_valid:
                return arr[i]

print(find_invalid(content_list))
