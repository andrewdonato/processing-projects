tileWall = 100
def setup():
    size(1201,601)
    background(255)

    
# def draw():
    # noCursor()
    frameRate(1)
    background(255)
    placeTiles()
    
    # rect(0,0,3*tileWall,3*tileWall)
    # translate(tileWall,tileWall)
    # scale(-1,1);
    # translate(-tileWall,)
    # createTile3(tileWall)
      

def placeTiles():        
    for y in range(0, height, tileWall):
        for x in range(0, width, tileWall):
            pushMatrix()
            
            translate(x, y)
            
            ## rotation
            flipChance = int(random(0,2))
            turns = int(random(0, 4))
            rotation = turns * 90                            
            rotate(radians(rotation))        
            if flipChance == 1:
                scale(-1,1);
                translate(-tileWall,0)   
                                             
            if rotation == 90:
                translate(0, -tileWall)
            elif rotation == 180:
                translate(-tileWall, -tileWall)
            elif rotation == 270 :
                translate(-tileWall, 0)                                           
            
            createTile(tileWall)
                
            popMatrix()
    
def keyReleased():
    global tileWall

    if key == "=" or key == "+" :      
        tileWall += 10
    elif key == "-" or key == "_" :
        if tileWall > 10 :      
            tileWall -= 10
        


                                          
                        
                                                

def createTile(tileWall):        
    noFill()
    ## tile outline
    rect(0,0,tileWall,tileWall)
    ## inside circle
    arc(0,0,tileWall/2,tileWall/2, 0, HALF_PI)
    ## square star corner
    line(0, 3*tileWall/4, tileWall/4, tileWall/2)
    line(tileWall/4, tileWall/2, tileWall/2, tileWall/2)
    line(tileWall/2, tileWall/2, tileWall/2, tileWall/4)
    line(3*tileWall/4, 0, tileWall/2, tileWall/4)
    ## round star corner
    line(tileWall/4, tileWall, tileWall/2, 3*tileWall/4)
    arc(3*tileWall/4, 3*tileWall/4, tileWall/2, tileWall/2, PI, PI+HALF_PI)
    line(tileWall, tileWall/4, 3*tileWall/4, tileWall/2)
    ## inside square
    line(3*tileWall/4, tileWall, 3*tileWall/4, 3*tileWall/4)
    line(tileWall,3*tileWall/4, 3*tileWall/4, 3*tileWall/4)
    

def createTile1(tileWall):
    noFill()
    line(tileWall/4, 0, tileWall/2, tileWall/4)

    
def createTile2(tileWall):
    noFill()
    # rect(0,0,tileWall,tileWall)
    ## top left triangle
    line(tileWall/4, 0, tileWall/2, tileWall/4)
    line(tileWall/2, 0, tileWall/2, tileWall/4)
    ## top right triangle
    line(3*tileWall/4, 0, tileWall, tileWall/4)
    ## blade thing
    line(0, tileWall/4, tileWall/4, tileWall/4)
    line(tileWall/4, tileWall/4, tileWall/2, tileWall/2)
    line(0, tileWall/2, tileWall/2, tileWall/2)
    line(tileWall/4, 3*tileWall/4, tileWall/2, tileWall/2)
    line(0, 3*tileWall/4, tileWall/4, 3*tileWall/4)
    ## across from blade
    line(tileWall, tileWall/2, 3*tileWall/4, tileWall/4)
    line(3*tileWall/4, tileWall/4, 3*tileWall/4, tileWall/2)
    line(3*tileWall/4, tileWall/2, tileWall, 3*tileWall/4)
    ## bottom left triangle
    line(0, 3*tileWall/4, tileWall/4, tileWall)
    ## bottom rectangle
    line(tileWall/4, tileWall, tileWall/2, 3*tileWall/4)
    line(tileWall/2, 3*tileWall/4, 3*tileWall/4, 3*tileWall/4)
    line(3*tileWall/4, 3*tileWall/4, 3*tileWall/4, tileWall)
    
def createTile3(tileWall):
    noFill()
    stroke(255,0,0)
    rect(0,0,tileWall,tileWall)
    rect(tileWall,tileWall,tileWall,tileWall)
    stroke(0)
    # scale(-1,1)
    # rect(tileWall,tileWall,tileWall,tileWall)
            
