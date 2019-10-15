## Before cleanup

# Question: You are given a 2d array filled with 1s and 0s.
# A 0 represents water and a 1 represents land (see figure below).
# Connected 1's represent a single island.
# Write a function to find the number of islands from a given 2d array.
# https://www.geeksforgeeks.org/find-number-of-islands/
# https://www.reddit.com/r/csinterviewproblems/comments/3xdmp6/count_number_of_islands/

# I know each landUnit and their adjacent squares. 
# Now I just need to find out when others are in their adjacent squares

bigMap = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
          [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
          [0, 0, 1, 1, 0, 1, 0, 0, 1, 1]]

easyMap = [[1,1,0,0],
           [0,1,0,0],
           [0,0,0,1]]   

easierMap = [[1,0],
             [1,0]]
                
binaryMap = bigMap     

## draws the map
def showMap(binaryMap):
    # for j in 
    print " 0  1  2  3"
    for i in range(len(binaryMap)):
        row = binaryMap[i]
        print "%s    %s" %(row, i)

# output = 5 including diagonals, 6 NOT including diagonals

# numberOfIslands = 0
landCount = 0
landUnits = []
islands = []
islandCount = 0
timesTraveled = 0

class LandUnit():

    def __init__(self, i, j):
        self.i = self.y = i
        self.j = self.x = j
        self.address = [i, j]
        self.adjacentTopLeft        = [i - 1, j - 1]
        self.adjacentTop            = [i - 1, j]
        self.adjacentTopRight       = [i - 1, j + 1]
        self.adjacentRight          = [i    , j + 1]
        self.adjacentBottomRight    = [i + 1, j + 1]
        self.adjacentBottom         = [i + 1, j]
        self.adjacentBottomLeft     = [i + 1, j - 1]
        self.adjacentLeft           = [i    , j - 1]
        self.adjacentSquares = [self.adjacentTopLeft, self.adjacentTop, self.adjacentTopRight, self.adjacentRight, self.adjacentBottomRight, self.adjacentBottom, self.adjacentBottomLeft, self.adjacentLeft]
        self.followingAdjacentSquares = [self.adjacentRight, self.adjacentBottomLeft, self.adjacentBottom, self.adjacentBottomRight]
        self.neighbors = []
        self.visited = False
        self.island = 0
        self.lookedForNeighbors = False

    def showAdjacentUnit(self) :
        print "I am square: [%s, %s]" %(self.i, self.j)
        print "These are my newNeighborSquares : %s " %(self.followingAdjacentSquares)
        # print "This is my adjacentTop : %s " %(self.adjacentTop)
        # print "This is my adjacentBottom : %s " %(self.adjacentBottom)
        # print "This is my adjacentLeft : %s " %(self.adjacentLeft)
        # print "This is my adjacentRight : %s " %(self.adjacentRight)

    # def formIslands(self, landUnits):
    #     for landUnit in landUnits:
    #         for newNeighbor in self.followingAdjacentSquares:
    #             if landUnit.address == newNeighbor:
    #                 print "%s : %s is equal to %s" %(True, str(landUnit.address), newNeighbor)

    #             else:
    #                 pass
    #                 # print "%s : %s and %s" %(False, landUnit.address, newNeighbor)
                
        # check the adjacents against the list of landUnits
        # maybe create the islands here

def landCoordinateCollector():
    global landCount, landUnits
    for i in range(len(binaryMap)):
        for j in range(len(binaryMap[i])):
            ## Here I have the coordinate and if water or land
            print "y, x = [%s, %s] = %s" % (i, j, binaryMap[i][j])
            if binaryMap[i][j] == 1:
                landCount += 1
                landUnit = LandUnit(i, j)
                landUnits.append(landUnit)

        print "Count of landUnits at the end of row %s : %s" % (i, landCount)
    print "Length of landUnits array : %s" % len(landUnits)
    print "This is the list of landUnits : %s" % landUnits


def showAdjacent(landUnits):
    print "This is all of the landUnits at once, no filter : %s " %(landUnits)
    for landUnit in landUnits:
        landUnit.showAdjacentUnit()

def formIslands(landUnits):
    global islands, islandCount
    for i in range(len(landUnits)):
        landUnit = landUnits[i]        
        # print landUnit.visited
        if landUnit.lookedForNeighbors == False:
            findNeighbor(landUnit)
            islandCount += 1

def findNeighbor(landUnit):
    global timesTraveled, islandCount, islands
    timesTraveled += 1


    print "this is %s and I've traveled %s" %(landUnit.address, timesTraveled)
    # print timesTraveled
    # print "reached %s levels deep" %(timesTraveled)
    # if timesTraveled == 1:
    print "I have lookedForNeighbors : %s" %(landUnit.lookedForNeighbors)
        
    
    if landUnit.lookedForNeighbors == False:
        landUnit.lookedForNeighbors = True
    #     ## Find neighbors
        ## i am the node, I look around at my adjacents starting at the top left
        ## if I see someone, I say, hey look for neighbors
        ## then I go on and cool turning my head

        for i in range(len(landUnit.adjacentSquares)):
            adjacentSquare = landUnit.adjacentSquares[i]
            for j in range(len(landUnits)):
                possibleNeighbor = landUnits[j]
                if str(possibleNeighbor.address) == str(adjacentSquare):
                    landUnit.neighbors.append(possibleNeighbor)
                    findNeighbor(possibleNeighbor)
        # landUnit.lookedForNeighbors = True
        print "Having completed the search, %s just finished looking for my neighbors and these are them" %(landUnit.address)
        print landUnit.neighbors
    else:
        # islandCount += 1
        pass

landCoordinateCollector()
# showAdjacent(landUnits)
formIslands(landUnits)
showMap(binaryMap)
print "islandCount == %s" %(islandCount)
