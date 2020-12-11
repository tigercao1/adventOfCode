myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

content_list = list(int(i) for i in content_list)

content_list.sort()
print(content_list)
def find_diff(arr):
    diff_one_count = 0
    diff_three_count = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            diff_one_count += 1
        elif arr[i] == arr[i-1] + 3:
            diff_three_count += 1
    print(diff_one_count, diff_three_count)
    return (diff_one_count+1) * (diff_three_count+1)

print(find_diff(content_list))