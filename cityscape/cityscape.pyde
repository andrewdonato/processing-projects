buildings = []

def setup():
    size(2000, 2000, P3D)
    camera(width/2.0, -height, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    createBuildings(middleStreet()[0], middleStreet()[1])
    
def draw():
    background(255)
    stroke(0)

    # camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    # camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0)
    # camera(width/2.0 + 2*mouseX, height/2.0 - 3*mouseY, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    
    
    # draw grid
    strokeWeight(1)
    showGrid()
    
    # draw street
    strokeWeight(5)
    line(*middleStreet()[0])
    line(*middleStreet()[1])
    
    # draw buildings
    strokeWeight(5)
    drawBuildings()
    
    camera(3*mouseX - width , 3*mouseY - height, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)


def showGrid():
    strokeWeight(1)
    x = 0
    while x < width :
        line(x, -height, 0, x, height, 0)
        x = x + 50
    
    y = -height
    while y < height :
        line(0, y, 0, width, y, 0)
        y = y + 50
    
    
def middleStreet():
    lineLeft = (width/2 - width/10, -height, 0, width/2 - width/10, height, 0)
    lineRight = (width/2 + width/10, -height, 0, width/2 + width/10, height, 0)
    return lineLeft, lineRight
    # line(*lineLeft)
    # line(*lineRight)
    
    
def createBuildings(leftSide, rightSide):
    global buildings
    strokeWeight(5)

    boxX = 50
    boxY = 100
    boxZ = 500
    
    
    translate(leftSide[0] - boxX/2, -height + boxY/2 , boxZ/2)
    box(boxX, boxY, boxZ)
    
    amount = 10
    i = 0
    while i < amount:
        
        boxX = int(random(500))
        boxY = int(random(500))
        boxZ = int(random(500))
        
    
        building = [boxX, boxY, boxZ]
        buildings.append(building)    
        translate(0, boxY + height/100, 0)
        i += 1
        
def drawBuildings():
    for building in buildings:
        
        box(building[0], building[1], building[2])
        
    
    
    
    
    
    
    
    
   
    
    
