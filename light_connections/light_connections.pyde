# lightPoints = ["a","b","c","d","e","f"]
lightPoints = []
# redSeed = int(random(255))
# greenSeed = int(random(255))
# blueSeed = int(random(255))

def setup():
    size (700, 700)
    background (0)
    cellStroke = 0
    stroke(255)
    
    ## generate random points 
    randomPoints()

        
def draw():
    background(0)
    strokeWeight(2)
    noCursor()
    point(mouseX,mouseY)
    for i in range(len(lightPoints)):
        beginLine = lightPoints[i] 
                
        ## draw a dot for each point in lightPoints
        strokeWeight(2)
        point(beginLine[0], beginLine[1])
            
        ## draws lines to mouse cursor
        strokeWeight(1)
        line(mouseX, mouseY, beginLine[0], beginLine[1])
        
        ## create lines from each point to every other point
        for j in range(i, len(lightPoints)):
            # strokeWeight(0)
            completeLine = lightPoints[j]
            ## line color
            stroke((completeLine[2]+beginLine[2])/2,(completeLine[3]+beginLine[3])/2, (completeLine[4]+beginLine[4])/2)
            
            line(beginLine[0], beginLine[1], completeLine[0], completeLine[1])
        
def mouseClicked():
    r = int(random(255))
    g = int(random(255))
    b = int(random(255))
    # print r,g,b
    lightPoints.append([mouseX, mouseY, r,g,b])
    
def randomPoints():
    ## seed max       1234567890123456
    seed = int(random(9999999999999999))
    print "randomSeed : %s" %seed
    
    
    randomSeed(seed)
    # randomSeed(seed)
    # randomSeed(2538053478383616)
    # randomSeed(8910780460171264)
    # randomSeed(3903994543996928)
    # randomSeed(1562722374254592)
    # randomSeed(351116764119040)
    # randomSeed(902055875051520)
    # randomSeed(542971678162944)
    # randomSeed(2816)
    
    for i in range(0, 5):
        x = int(random(width))
        y = int(random(height))
        r = int(random(255))
        g = int(random(255))
        b = int(random(255))
        # lightPoints.append([x,y)
        lightPoints.append([x,y,r,g,b])
        

def keyPressed():
    global lightPoints
    if len(lightPoints) > 0 :
        if key == "d" or key == "D" :
            del lightPoints[len(lightPoints) - 1]

                        
