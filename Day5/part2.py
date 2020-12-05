myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

def get_half(left, right, C):
    mid = (left + right) // 2
    if C == "B" or C == "R":
        return mid+1, right
    return left, mid


def find_seat(arr):
    seats = []
    for string in arr:
        lo_row = 0
        hi_row = 127
        lo_col = 0
        hi_col = 7
        for c in string[:-3]:
            lo_row, hi_row = get_half(lo_row, hi_row, c)
        
        for c in string[-3:]:
            lo_col, hi_col = get_half(lo_col, hi_col, c)
        seats.append(lo_row*8+lo_col)
    return seats

def find_my_seat(arr):
    arr.sort()
    count = 0
    for i in range(1, len(arr)):
        if arr[i] - 2 == arr[i-1]:
            return arr[i] - 1


print(find_my_seat(find_seat(content_list)))