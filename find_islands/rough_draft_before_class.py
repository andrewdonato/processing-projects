# Question: You are given a 2d array filled with 1s and 0s.
# A 0 represents water and a 1 represents land (see figure below).
# Connected 1's represent a single island.
# Write a function to find the number of islands from a given 2d array.
# https://www.geeksforgeeks.org/find-number-of-islands/
# https://www.reddit.com/r/csinterviewproblems/comments/3xdmp6/count_number_of_islands/

binaryMap = [[0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
             [0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
             [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
             [0, 0, 1, 1, 0, 1, 0, 0, 1, 1]]
# output = 5 including diagonals, 6 NOT including diagonals

# numberOfIslands = 0
landCount = 0
landUnits = []
islands = []

# this is getting messy so I am switching to a class
def landCoordinateCollector():
    global landCount, landUnits
    for i in range(len(binaryMap)):
        # print i
        for j in range(len(binaryMap[i])):
            print "y, x = [%s, %s] = %s" % (i, j, binaryMap[i][j])
            if binaryMap[i][j] == 1:
                landCount += 1
                landUnits.append([i, j])
            # print "Units of land : %s" %(landCount)
        print "Count of landUnits at the end of row %s : %s" % (i, landCount)
    print "Length of landUnits array : %s" % len(landUnits)
    print "This is the list of landUnits : %s" % landUnits
    # print landUnits


# this is getting messy so I am switching to a class
def islandMerge(landUnits):
    print landUnits
    for landCoordinate in landUnits:
        print landCoordinate

        adjacentTop = [landCoordinate[0] - 1, landCoordinate[1]]
        adjacentBottom = [landCoordinate[0] + 1, landCoordinate[1]]
        adjacentLeft = [landCoordinate[0], landCoordinate[1] - 1]
        adjacentRight = [landCoordinate[0] + 1, landCoordinate[1]]

        print "adjacentTop = %s" % adjacentTop

        # if len(islands) == 0:
        #     island = []
        #     island.append(landCoordinate)
        # else :
        #     pass


landCoordinateCollector()
islandMerge(landUnits)

class LandSquare():

    def __init__(self, i, j):
        self.y = self.i = i
        self.x = self.j = j

        self.adjacentTop
