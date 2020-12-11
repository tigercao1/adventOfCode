myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

l = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,-1],[1,1],[-1,1]]

import collections

def bound_check(curr, bound):
    return 0 <= curr < bound

def source_seats(arr):
    trow = len(arr)
    tcol = len(arr[0])
    output_seats = [[0 for i in range(tcol)] for i in range(trow)]
    seats = collections.deque([(0,0)])
    visited = set([0,0])
    count = 0

    while seats:
        row, col = seats.popleft()
        if arr[row][col] == "L":
            can_occupy = True
            for i in range(len(l)):
                if bound_check(row+l[i][0], trow) and bound_check(col+l[i][1], tcol) and arr[row+l[i][0]][col+l[i][1]] == "#":
                    can_occupy = False
            if can_occupy:
                output_seats[row][col] = "#"
            else:
                output_seats[row][col] = arr[row][col]

        if arr[row][col] == ".":
            output_seats[row][col] = arr[row][col]
        if arr[row][col] == "#":
            occupy_count = 0
            for i in range(len(l)):
                if bound_check(row+l[i][0], trow) and bound_check(col+l[i][1], tcol) and arr[row+l[i][0]][col+l[i][1]] == "#":
                    occupy_count += 1
            if occupy_count >= 4:
                output_seats[row][col] = "L"
            else:
                output_seats[row][col] = arr[row][col]

        if output_seats[row][col] == "#":
            count += 1

        for i in range(len(l)):
            if bound_check(row+l[i][0], trow) and bound_check(col+l[i][1], tcol) and (row+l[i][0], col+l[i][1]) not in visited:
                seats.append((row+l[i][0], col+l[i][1]))
                visited.add((row+l[i][0], col+l[i][1]))
    return count, output_seats

def find_occupied(arr):
    prev = 0
    curr_count, prev_arr = source_seats(arr)
    while prev != curr_count:
        
        prev = curr_count
        curr_count, prev_arr = source_seats(prev_arr)
        
    return prev-1

print(find_occupied(content_list))

'''
BFS

row col

search every immediate neighbours

rol-1 <= 0
col-1 <= 0
rol+1 < len(arr)
col+1 < len(arr[0])

rol+1 col
rol-1 col
row col+1
row col-1
row-1 col-1
row+1 col-1
row+1 col+1
row-1 col+1

'''