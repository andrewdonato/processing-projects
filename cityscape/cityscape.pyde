import math 

buildings1 = []
buildings2 = []
buildings3 = []
buildings4 = []

mapTop = 0
mapBottom = 0
mapleft = 0
mapRight = 0
alleyway = 5

def setup():
    global mapTop, mapBottom, mapleft, mapRight
    # global buildings, buildings1
    size(601, 601, P3D)
    mapTop = -height
    mapBottom = height
    mapleft = 0
    mapRight = width
    
    camera(width/2.0, -height, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    createBuildings(middleVerticalStreet()[0], "vertical", buildings1, 20)
    createBuildings(middleVerticalStreet()[0], "vertical", buildings2, 20)
    createBuildings(middleHorizontalStreet()[0], "horizontal", buildings3, 20)
    createBuildings(middleHorizontalStreet()[0], "horizontal", buildings4, 20)
    
    
def draw():
    global buildings, buildings1
    background(255)
    stroke(0)

    # draw grid
    strokeWeight(1)
    showGrid()
    
    # draw street
    strokeWeight(5)
    line(*middleVerticalStreet()[0])
    line(*middleVerticalStreet()[1])
    line(*middleHorizontalStreet()[0])
    line(*middleHorizontalStreet()[1])
    
    # draw buildings
    strokeWeight(5)
    drawBuildings(middleVerticalStreet()[0], buildings1, "left")
    drawBuildings(middleVerticalStreet()[1], buildings2, "right")
    drawBuildings(middleHorizontalStreet()[0], buildings3, "above")
    drawBuildings(middleHorizontalStreet()[1], buildings4, "below")

    # camera
    camera(3*mouseX - width , 2*mouseY - height, 1*(height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, height/2, 0, 1, 0)


def showGrid():
    strokeWeight(1)
    x = 0
    while x < width :
        line(x, 0, 0, x, 0, height)
        # line(x, 0, -height, x, 0, height)
        x = x + 50
    
    # z = -height
    z = 0
    while z < height :
        line(0, 0, z, width, 0, z)
        z = z + 50
    
    strokeWeight(5)
    line(mapleft, 0, 0, mapRight, 0 , 0)
    
def middleVerticalStreet():
    # lineLeft = (width/2 - width/10, 0, -height, width/2 - width/10, 0, height)
    # lineRight = (width/2 + width/10, 0,  -height, width/2 + width/10, 0, height)
    # lineLeft = (width/2 - width/10, 0, 0, width/2 - width/10, 0, height)
    # lineRight = (width/2 + width/10, 0,  0, width/2 + width/10, 0, height)
    # lineLeft = (width/2 - width/20, 0, 0, width/2 - width/20, 0, height)
    # lineRight = (width/2 + width/20, 0,  0, width/2 + width/20, 0, height)
    lineLeft = (width/2 - width/40, 0, 0, width/2 - width/40, 0, height)
    lineRight = (width/2 + width/40, 0,  0, width/2 + width/40, 0, height)
    
    return lineLeft, lineRight
    # line(*lineLeft)
    # line(*lineRight)

def middleHorizontalStreet():
    lineUp = (0, 0, height/2 - height/40, width, 0, height/2 - height/40)
    lineDown = (0, 0, height/2 + height/40, width, 0, height/2 + height/40)
    
    return lineUp, lineDown    
    
def createBuildings(lineSegment, orientation, buildingArray=buildings1, amount=15):
    global buildings
    strokeWeight(5)
    # boxX = 50
    # boxY = 100
    # boxZ = 500
    
    # box(boxX, boxY, boxZ)
    
    # amount = 15
    
    # determine magnitude of line    
    xAbsolute = abs(lineSegment[0]-lineSegment[3])
    yAbsolute = abs(lineSegment[1]-lineSegment[4])
    zAbsolute = abs(lineSegment[2]-lineSegment[5])
    lineMagnitude = math.sqrt(xAbsolute**2 + yAbsolute**2 + zAbsolute**2)

    print orientation
    # i = 0
    buildingMagnitude = 0    
    # while i < amount:
    while buildingMagnitude < lineMagnitude :
        
        boxX = int(random(10, height/10))
        boxY = int(random(10, height/10))
        boxZ = int(random(10, height/10))
        # boxX = 50
        # boxY = 50
        # boxZ = 50
        
        if orientation == "horizontal" :
            buildingMagnitude += boxX + alleyway
            # buildingMagnitude == boxZ + buildingMagnitude
        elif orientation == "vertical" :
            buildingMagnitude += boxZ + alleyway
            # buildingMagnitude == boxZ + buildingMagnitude
        # print buildingMagnitude
        
        if buildingMagnitude < lineMagnitude :
            building = [boxX, boxY, boxZ]
            buildingArray.append(building)    
        
        # i += 1
    print len(buildingArray)         
def drawBuildings(streetLine, buildingArray, side):
    buildings = buildingArray
    pushMatrix()
        
    for i in range(len(buildings)):
        
        if i == 0 :
            previousBuilding = [0, 0, 0]
        else:
            previousBuilding = buildings[i-1]
        
        building = buildings[i]
        
        boxX = building[0]
        boxY = building[1]
        boxZ = building[2]

        # pushMatrix()

        if side == "left" or side == "right":
            # moves buildings along the Z axis down the street
            translate(0, 0, previousBuilding[2]/2+ boxZ/2 + alleyway )
            # popMatrix()
        
            if side == "left":
                            
                # # moves buildings along the Z axis down the street
                # translate(0, 0, previousBuilding[2]/2+ boxZ/2 + 5 )
                    
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(streetLine[0] - boxX/2, -boxY/2, 0)                        
                
                # translate(0, boxY + height/100, 0)
                box(building[0], building[1], building[2])
                popMatrix()
                    
            elif side == "right":
                # # moves buildings along the Z axis down the street
                # translate(0, 0, previousBuilding[2]/2+ boxZ/2 + 5 )
                    
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(streetLine[0] + boxX/2, -boxY/2, 0)                        
                
                # translate(0, boxY + height/100, 0)
                box(building[0], building[1], building[2])
                popMatrix()
                
        elif side == "above" or side == "below":
            # moves buildings along the Z axis down the street
            translate(previousBuilding[0]/2+ boxX/2 + alleyway, 0, 0)
            # popMatrix()
                            
            if side == "above":
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(0, -boxY/2, streetLine[2] - boxZ/2)                        
                
                # translate(0, boxY + height/100, 0)
                box(building[0], building[1], building[2])
                popMatrix()
                
            elif side == "below":
                pushMatrix()
                
                # moves buildings against the street and adjusts height
                translate(0, -boxY/2, streetLine[2] + boxZ/2)                        
                
                # translate(0, boxY + height/100, 0)
                box(building[0], building[1], building[2])
                popMatrix()
            
    popMatrix()
    
    
    
    
    
   
    
    
