def setup():
    size(1000, 1000, P3D)
    
    
def draw():
    background(255)
    stroke(0)

    # camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    # camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0)
    camera(width/2.0, height/2.0 + mouseY, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/10.0, 0, 0, 1, 0)
    showGrid()
    middleStreet()
    createBuildings()

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
    strokeWeight(5)
    lineLeft = (width/2 - width/10, -height, 0, width/2 - width/10, height, 0)
    lineRight = (width/2 + width/10, -height, 0, width/2 + width/10, height, 0)
    line(*lineLeft)
    line(*lineRight)
    
def createBuildings():
    strokeWeight(5)
    # amount=1
    # for i in range(amount):
    # translate()
    box(50,100,500)
    
    
