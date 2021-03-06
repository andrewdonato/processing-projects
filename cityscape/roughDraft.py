buildings = []



def setup():
    size(700, 700, P3D)
    mapTop = -height
    mapBottom = height
    mapleft = 0
    mapRight = width
    
    camera(width/2.0, -height, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    createBuildings(middleStreet()[0], middleStreet()[1])
    
def draw():
    background(255)
    stroke(0)

    # draw grid
    strokeWeight(1)
    showGrid()
    
    # draw street
    strokeWeight(5)
    line(*middleStreet()[0])
    line(*middleStreet()[1])
    
    # draw buildings
    strokeWeight(5)
    drawBuildings(middleStreet()[0], middleStreet()[1])
    
    # camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    # camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0)
    # camera(width/2.0 + 2*mouseX, height/2.0 - 3*mouseY, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
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
    
    box(boxX, boxY, boxZ)
    
    amount = 10
    i = 0
    while i < amount:
        
        # boxX = int(random(height/4))
        # boxY = int(random(height/4))
        # boxZ = int(random(height/4))
        boxX = 50
        boxY = 100
        boxZ = 500
    
        building = [boxX, boxY, boxZ]
        buildings.append(building)    
        
        i += 1
        
def drawBuildings(leftSide, rightSide):
    
    translate(leftSide[0] - 50/2, -height + 100/2 , 500/2)
    for building in buildings:
        
        boxX = building[0]
        boxY = building[1]
        boxZ = building[2]
        
        # pushMatrix()
        # translate(leftSide[0] - boxX/2, -height + boxY/2 , boxZ/2)
        
        
        translate(0, boxY + height/100, 0)
        box(building[0], building[1], building[2])
        # popMatrix()
        
    
class Building:
    def __init__ (self, width, height, depth, positioningToStreet):
        self.w = width
        self.h = height
        self.d = depth
        self.x = None
        self.y = None
        self.z = None
        self.side = positioningToStreet  #left, right, up, down    
        
        
class Street:
    def __init__ (self, lineOne, linetwo, start, finish):
        self.angle = angle 
        self.lineOne = firstEdge
        self.linetwo = secondEdge
        self.lineOneBuildings = []
        self.linetwoBuildings = []
        
    # def placeBuildings(self):
    #     pushMatrix()
        
    #     translate(edge - self.w/2, -height + boxY/2 , boxZ/2)
    #     translate()
    
    
    
    
    
   
    
    
