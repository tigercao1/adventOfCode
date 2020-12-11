myfile = open("input.txt", "r")
content = myfile.read()
content_list = content.split("\n")
myfile.close()

content_list = list(int(i) for i in content_list)

content_list.sort()

def find_diff(arr):
    diff_one_count = 0
    diff_three_count = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            diff_one_count += 1
        elif arr[i] == arr[i-1] + 3:
            diff_three_count += 1
    return (diff_one_count) * (diff_three_count)

print(find_diff([0] + content_list + [content_list[-1] + 3]))

def find_distinct_ways(arr):
    # dp array to store the number of combinations we can get for arr[i]
    dp = [0 for i in range(len(arr))]
    # There is only 1 combination for arr[-1]
    dp[len(arr) - 1] = 1
    # backward iteration
    for i in range(len(arr)-2, -1 ,-1):
        # combine the number of combinations from arr[i] to arr[i+k] satisfying arr[i+k] - arr[i] <= 3
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] <= 3:
                # store the accumulated number of combinations for arr[i] at dp[i]
                dp[i] += dp[j]
            else:
                # since arr[i+k] - arr[i] is larger than 3, move i backward
                break
    return dp[0]

print(find_distinct_ways([0] + content_list + [content_list[-1] + 3]))
    




'''
Jibrish below, thought way too hard getting my head around a distinct ways dp solution...

131, 4,       4,                       2,                       1,                  1                     1]
131, 132,     135,                     136                      137,                138,                  141]
131, dp[135], dp[135] += dp[136..138], dp[136] += dp[137..138], dp[137] += dp[138], dp[138] += dp[141]    1]

if distance is 3, find number of combinations between these 2 numbers

138
137,138


141, 138

1

dp[138] = 1

dp[137] = math.comb(1,1) + dp[138]

dp[136] += math.comb(2,1) + dp[138]
dp[136] += math.comb(2,2) + dp[138]
dp[135] += math.comb(3,1) + dp [138]
dp[135] += math.comb(3,2) + dp [138]
dp[135] += math.comb(3,3) + dp[138]

141, 138

138,137,136,135

135,132

132,131,130,129

128,131

141, 137

2 + 1 -> 3

141,138,137

141, 137

141, 138

141,138,137,136

141, 137, 136

141, 138, 136

141, 136

4 + 3 -> 7

135, 136, 137, 138

4

if curr num cannot reach 141
find num of combinations of 136,137,138
3c1 + 3c2 + 3c3

132, 135, 136, 137, 138, 141




math.comb(3)

1

1 + 2 -> 3




start from 0, add 1 or 2 or 3. if each number in path 

base case -> 1 way
include 0 -> 1 + 1 way -> 2
include 1 -> 2 + 2 -> 4
include 2 -> 2 + 4 -> 6
include 3 -> 0 + 6 -> 6

storing how many ways we can get for each number in the list

target = 141

ways to reach 141 given an arr where max diff is 3




132, 135, 136, 137, 138, 141

141, 138, 135, 

[0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 21, 22,

0, 1, 2, 3, 4, 7    8, 9, 10, 11, 14

1,2,3,4,7

2,3,4,7
3,4,7

1,3,4,7

3,4,7
1,4,7
2,4,7



we have 68 1 diff adpaters

have 23 3 diff adapters,

between 

'''