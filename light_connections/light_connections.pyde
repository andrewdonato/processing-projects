# lightPoints = ["a","b","c","d","e","f"]
lightPoints = []

def setup():
    size (1400, 700)
    background (0)
    cellStroke = 0
    stroke(255)
    
    randomPoints()
    
        
def draw():
    background(0)
    strokeWeight(2)
    noCursor()
    point(mouseX,mouseY)
    for i in range(len(lightPoints)):
        beginLine = lightPoints[i] 
        
        ## cursor point and lines to cursor
        strokeWeight(2)
        point(beginLine[0], beginLine[1])
        strokeWeight(0)
        line(mouseX, mouseY, beginLine[0], beginLine[1])
        
        ## create lines from each point to every other point
        for j in range(i, len(lightPoints)):
            # stroke(int(random(255))
            strokeWeight(0)
            completeLine = lightPoints[j]
            
            # randomSeed(100)
            # stroke(int(random(255)), int(random(255)), int(random(255)))
            
            line(beginLine[0], beginLine[1], completeLine[0], completeLine[1])
        
def mouseClicked():
    lightPoints.append([mouseX, mouseY])
    
def randomPoints():
    ## seed max       1234567890123456
    seed = int(random(9999999999999999))
    print "randomSeed : %s" %seed
    
    
    randomSeed(seed)
    # randomSeed(seed)
    # randomSeed(seed)
    # randomSeed(seed)
    # randomSeed(3903994543996928)
    # randomSeed(1562722374254592)
    # randomSeed(351116764119040)
    # randomSeed(902055875051520)
    # randomSeed(542971678162944)
    # randomSeed(2816)
    
    for i in range(0, 15):
        x = int(random(width))
        y = int(random(height))
        lightPoints.append([x,y])
        

def keyPressed():
    global lightPoints
    if len(lightPoints) > 0 :
        if key == "d" or key == "D" :
            del lightPoints[len(lightPoints) - 1]

                        
