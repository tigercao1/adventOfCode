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

#Sliding window
def find_sum(arr):
    invalid = find_invalid(arr)
    p1, p2 = 0, 1
    curr_sum = arr[p1] + arr[p2]
    iterations = 0
    while p2 < len(arr)-1:
        iterations += 1
        if curr_sum < invalid:
            p2 += 1
            curr_sum += arr[p2]
        elif curr_sum > invalid:
            curr_sum -= arr[p1]
            p1 += 1
        else:
            print(iterations)
            return arr[p1:p2+1]
    return []


def find_max_min(arr):
    return max(arr) + min(arr)

print(find_max_min(find_sum(content_list)))




