# Question: You are given a 2d array filled with 1s and 0s.
# A 0 represents water and a 1 represents land (see figure below).
# Connected 1's represent a single island.
# Write a function to find the number of islands from a given 2d array.
# https://www.geeksforgeeks.org/find-number-of-islands/
# https://www.reddit.com/r/csinterviewproblems/comments/3xdmp6/count_number_of_islands/

# I know each landUnit and their adjacent squares. 
# Now I just need to find out when others are in their adjacent squares

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
islands = [[]]


class LandUnit():

    def __init__(self, i, j):
        self.i = self.y = i
        self.j = self.x = j
        self.address = [i, j]
        self.adjacentTop = [i - 1, j]
        self.adjacentBottom = [i + 1, j]
        self.adjacentLeft = [i, j - 1]
        self.adjacentRight = [i + 1, j]
        self.adjacentTopLeft = [i - 1, j - 1]
        self.adjacentTopRight = [i - 1, j + 1]
        self.adjacentBottomLeft = [i + 1, j - 1]
        self.adjacentBottomRight = [i + 1, j + 1]
        self.neighborSquares = [self.adjacentTop, self.adjacentBottom, self.adjacentLeft, self.adjacentRight, self.adjacentTopLeft, self.adjacentTopRight, self.adjacentBottomLeft, self.adjacentBottomRight]
        self.newNeighborSquares = [self.adjacentBottom, self.adjacentRight, self.adjacentBottomLeft, self.adjacentBottomRight]
        self.neighbors = []

        self.island = 0

    def showAdjacentUnit(self) :
        print "I am square: [%s, %s]" %(self.i, self.j)
        print "These are my newNeighborSquares : %s " %(self.newNeighborSquares)
        # print "This is my adjacentTop : %s " %(self.adjacentTop)
        # print "This is my adjacentBottom : %s " %(self.adjacentBottom)
        # print "This is my adjacentLeft : %s " %(self.adjacentLeft)
        # print "This is my adjacentRight : %s " %(self.adjacentRight)

    # def formIslands(self, landUnits):
    #     for landUnit in landUnits:
    #         for newNeighbor in self.newNeighborSquares:
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

def formIslands(landUnits, islands):
    for i in range(len(landUnits)):
        landUnit = landUnits[i]

        # for j in range(len(landUnit.neighborSquares)):

        # landUnit.formIslands(landUnits) 
        # if len(islands) == 0:
        #     islands.append([landUnit.address])
        #     print "this is islands: %s" %(islands)
        
        # matchingNeigbors = [j for j in landUnits + landUnit.newNeighborSquares if j in landUnits and j in landUnit.newNeighborSquares]
        #         print "These are my matchingNeigbors : %s" %(matchingNeigbors)
        # matchingNeigbors =


        for j in range(len(landUnit.neighborSquares)):
            newNeighborSquare = landUnit.neighborSquares[j]

            # print "------------------------------------------"
            # print "%s and %s" %(str(landUnit.address), newNeighborSquare)
            
            for k in range(i+1,len(landUnits)):
                possibleNeighbor = landUnits[k]
                if str(possibleNeighbor.address) == str(newNeighborSquare):
                    print "I am landUnit: %s" %(landUnit.address)
                    print "%s : possibleNeighbor:%s is equal to newNeighborSquare:%s" %(True, str(possibleNeighbor.address), newNeighborSquare)
                    landUnit.neighbors.append(possibleNeighbor.address)

                else:
                    pass
                    # print "%s : %s and %s" %(False, landUnit.address, newNeighbor)


landCoordinateCollector()
# showAdjacent(landUnits)
formIslands(landUnits, islands)

