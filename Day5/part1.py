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
    max_seat = float('-inf')
    for string in arr:
        lo_row = 0
        hi_row = 127
        lo_col = 0
        hi_col = 7
        for c in string[:-3]:
            lo_row, hi_row = get_half(lo_row, hi_row, c)
            print(lo_row, hi_row)
        
        for c in string[-3:]:
            lo_col, hi_col = get_half(lo_col, hi_col, c)
        max_seat = max(max_seat, lo_row*8+lo_col)
    return max_seat


print(find_seat(content_list))