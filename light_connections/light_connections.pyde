import math

seedLines = 50
allowedRadius = 150
rangeStep = 10

# lightPoints = ["a","b","c","d","e","f"]
lightPoints = []
finite = False
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
        if finite == False:
            line(mouseX, mouseY, beginLine[0], beginLine[1])
        elif finite == True:            
            dotRange = calculateDistance(mouseX, mouseY, beginLine[0], beginLine[1])
            if dotRange <= allowedRadius:                
                line(mouseX, mouseY, beginLine[0], beginLine[1])
        
        ## create lines from each point to every other point
        for j in range(i, len(lightPoints)):
            # strokeWeight(0)
            completeLine = lightPoints[j]
            ## line color
            stroke((completeLine[2]+beginLine[2])/2,(completeLine[3]+beginLine[3])/2, (completeLine[4]+beginLine[4])/2)
            if finite == False:
                line(beginLine[0], beginLine[1], completeLine[0], completeLine[1])
            elif finite == True:
                dotRange = calculateDistance(beginLine[0], beginLine[1], completeLine[0], completeLine[1])
                if dotRange <= allowedRadius:                
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
    print "randomSeed(%s)" %seed
    
    randomSeed(seed)
    # randomSeed(seed)
    # randomSeed(2538053478383616)
    # randomSeed(8910780460171264)
    # randomSeed(3903994543996928)
    # randomSeed(1562722374254592)
    # randomSeed(351116764119040)
    # randomSeed(902055875051520)
    # randomSeed(542971678162944)
    # randomSeed(8604295888896000)
    # randomSeed(2816)
    # randomSeed(3812149352726528)
    
    for i in range(0, seedLines):
        x = int(random(width))
        y = int(random(height))
        r = int(random(255))
        g = int(random(255))
        b = int(random(255))
        # lightPoints.append([x,y)
        lightPoints.append([x,y,r,g,b])
        
def calculateDistance(aDotX, aDotY, bDotX, bDotY):
    aDotX, aDotY, bDotX, bDotY
    
    distance = math.sqrt((aDotX- bDotX)**2 +(aDotY - bDotY)**2)
    return distance
    

def keyPressed():
    global lightPoints, finite, allowedRadius
    if len(lightPoints) > 0 :
        if key == "d" or key == "D" :
            del lightPoints[len(lightPoints) - 1]
        
        if key == 'o' or key == 'O' :
            print ""
            for each in lightPoints:
                print("point(%s, %s)" %(each[0], each[1]))

        if key == 'p' or key == 'P' :
            print ""
            for each in lightPoints:
                fractionOfMaxX = float(each[0]/width)
                fractionOfMaxY = float(each[1]/height)
                print("point(%s * width, %s * height)" %(fractionOfMaxX, fractionOfMaxY))
                

        if key == " ":
            if finite == False:
                finite = True
            elif finite == True :
                finite = False 
                
        if key == '+' or key == '=' :
            allowedRadius += rangeStep
            
        if key == '-' or key == '_' :
            allowedRadius -= rangeStep
            if allowedRadius < 0:
                allowedRadius = 0
        
            
            

                        
