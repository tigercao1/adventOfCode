myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

l = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,-1],[1,1],[-1,1]]

import collections
from pprint import pprint

def bound_check(curr, bound):
    return 0 <= curr < bound

def source_seats(arr):
    trow = len(arr)
    tcol = len(arr[0])
    output_seats = [[0 for i in range(tcol)] for i in range(trow)]
    seats = collections.deque([(0,0)]) # queue
    visited = set([0,0])
    count = 0
    # BFS with queue
    while seats:
        row, col = seats.popleft()
        if arr[row][col] == "L":
            can_occupy = True
            for i in range(len(l)):
                temprow = row+l[i][0]
                tempcol = col+l[i][1]
                while bound_check(temprow, trow) and bound_check(tempcol, tcol):
                    if arr[temprow][tempcol] == "L":
                        break
                    if arr[temprow][tempcol] == "#":
                        can_occupy = False
                        break
                    temprow += l[i][0]
                    tempcol += l[i][1]
            if can_occupy:
                output_seats[row][col] = "#"
            else:
                output_seats[row][col] = arr[row][col]

        if arr[row][col] == ".":
            output_seats[row][col] = arr[row][col]
        if arr[row][col] == "#":
            occupy_count = 0
            for i in range(len(l)):
                temprow = row+l[i][0]
                tempcol = col+l[i][1]
                while bound_check(temprow, trow) and bound_check(tempcol, tcol):
                    if arr[temprow][tempcol] == "L":
                        break
                    if arr[temprow][tempcol] == "#":
                        occupy_count += 1
                        break
                    temprow += l[i][0]
                    tempcol += l[i][1]
            if occupy_count >= 5:
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