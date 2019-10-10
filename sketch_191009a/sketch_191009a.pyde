# Question: You are given a 2d array filled with 1s and 0s. 
# A 0 represents water and a 1 represents land (see figure below). 
# Connected 1's represent a single island. 
# Write a function to find the number of islands from a given 2d array.
# https://www.geeksforgeeks.org/find-number-of-islands/
# https://www.reddit.com/r/csinterviewproblems/comments/3xdmp6/count_number_of_islands/

binaryMap = [[0,0,1,0,1,1,0,0,1,0],
             [0,1,1,1,1,0,0,1,1,0],
             [0,0,1,1,1,1,0,0,1,1],
             [1,0,0,0,0,0,0,0,0,0],
             [0,0,1,1,1,0,0,0,1,1],
             [0,0,1,1,0,1,0,0,1,1]]
# output = 5 including diagonals, 6 NOT including diagonals

count = 0
for i in binaryMap : 
    # print i
    for j in i:
        if j == 1:
            count += 1
        print count
            
        # print j
