tileWall = 100
def setup():
    size(1201,601)
    background(255)

    
def draw():
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
            
            ## flip
            flipChance = int(random(0,2))                    
            if flipChance == 1:
                scale(-1,1);
                translate(-tileWall,0)   

                                             
            ## rotation                                                                              
            turns = int(random(0, 4))
            rotation = turns * 90                            
            rotate(radians(rotation))                                                                                                                                                                        
            if rotation == 90:
                translate(0, -tileWall)
            elif rotation == 180:
                translate(-tileWall, -tileWall)
            elif rotation == 270 :
                translate(-tileWall, 0)                                           
            
            strokeWeight(3)
            noFill()
            # stroke(200)
            # rect(0,0,tileWall,tileWall)
            stroke(0)
            createTile7(tileWall)
                
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
    stroke(200)
    # rect(0,0,tileWall,tileWall)

    # line(*tileWall/8, *tileWall/8, *tileWall/8, *tileWall/8)
    stroke(0)
    ## center line
    line(4*tileWall/8, 0*tileWall/8, 4*tileWall/8, 8*tileWall/8)
    
    ## top left quadrant
    ## vertical
    line(1*tileWall/8, 0*tileWall/8, 1*tileWall/8, 2*tileWall/8)
    line(2*tileWall/8, 0*tileWall/8, 2*tileWall/8, 3*tileWall/8)
    line(3*tileWall/8, 0*tileWall/8, 3*tileWall/8, 4*tileWall/8)
    ## horizontal
    line(0*tileWall/8, 1*tileWall/8, 1*tileWall/8, 1*tileWall/8)
    line(0*tileWall/8, 2*tileWall/8, 2*tileWall/8, 2*tileWall/8)
    line(0*tileWall/8, 3*tileWall/8, 3*tileWall/8, 3*tileWall/8)
    line(0*tileWall/8, 4*tileWall/8, 4*tileWall/8, 4*tileWall/8)

    ## top right quadrant
    ## vertical
    line(5*tileWall/8, 0*tileWall/8, 5*tileWall/8, 4*tileWall/8)
    line(6*tileWall/8, 0*tileWall/8, 6*tileWall/8, 3*tileWall/8)
    line(7*tileWall/8, 0*tileWall/8, 7*tileWall/8, 2*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 8*tileWall/8, 1*tileWall/8)
    
    ## horizontal
    line(7*tileWall/8, 2*tileWall/8, 8*tileWall/8, 2*tileWall/8)
    line(6*tileWall/8, 3*tileWall/8, 8*tileWall/8, 3*tileWall/8)
    line(5*tileWall/8, 4*tileWall/8, 8*tileWall/8, 4*tileWall/8)
    
    ## bottom left quadrant
    ## vertical
    line(1*tileWall/8, 7*tileWall/8, 1*tileWall/8, 8*tileWall/8)
    line(2*tileWall/8, 6*tileWall/8, 2*tileWall/8, 8*tileWall/8)
    line(3*tileWall/8, 5*tileWall/8, 3*tileWall/8, 8*tileWall/8)
    ## horizontal
    line(0*tileWall/8, 5*tileWall/8, 3*tileWall/8, 5*tileWall/8)
    line(0*tileWall/8, 6*tileWall/8, 2*tileWall/8, 6*tileWall/8)
    line(0*tileWall/8, 7*tileWall/8, 1*tileWall/8, 7*tileWall/8)
    
    ## bottom right quadrant
    ## vertical
    line(5*tileWall/8, 5*tileWall/8, 5*tileWall/8, 8*tileWall/8)
    line(6*tileWall/8, 5*tileWall/8, 6*tileWall/8, 7*tileWall/8)
    ## horizontal
    line(6*tileWall/8, 5*tileWall/8, 8*tileWall/8, 5*tileWall/8)
    line(7*tileWall/8, 6*tileWall/8, 8*tileWall/8, 6*tileWall/8)
    line(6*tileWall/8, 7*tileWall/8, 8*tileWall/8, 7*tileWall/8)
    
    
def createTile4(tileWall):
    
    line(4*tileWall/8, 0*tileWall/8, 4*tileWall/8, 4*tileWall/8)
    line(4*tileWall/8, 4*tileWall/8, 0*tileWall/8, 4*tileWall/8)
    line(0*tileWall/8, 5*tileWall/8, 2*tileWall/8, 5*tileWall/8)
    line(2*tileWall/8, 5*tileWall/8, 2*tileWall/8, 8*tileWall/8)
    line(1*tileWall/8, 6*tileWall/8, 1*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 6*tileWall/8, 1*tileWall/8, 6*tileWall/8)
    line(0*tileWall/8, 7*tileWall/8, 0*tileWall/8, 8*tileWall/8)
    line(8*tileWall/8, 5*tileWall/8, 3*tileWall/8, 5*tileWall/8)
    line(3*tileWall/8, 6*tileWall/8, 8*tileWall/8, 6*tileWall/8)
    line(5*tileWall/8, 6*tileWall/8, 5*tileWall/8, 8*tileWall/8)
    line(3*tileWall/8, 7*tileWall/8, 3*tileWall/8, 8*tileWall/8)
    line(3*tileWall/8, 7*tileWall/8, 4*tileWall/8, 7*tileWall/8)
    line(4*tileWall/8, 7*tileWall/8, 4*tileWall/8, 8*tileWall/8)
    line(8*tileWall/8, 7*tileWall/8, 6*tileWall/8, 7*tileWall/8)
    line(6*tileWall/8, 8*tileWall/8, 7*tileWall/8, 8*tileWall/8)
    line(5*tileWall/8, 0*tileWall/8, 5*tileWall/8, 2*tileWall/8)
    line(5*tileWall/8, 2*tileWall/8, 8*tileWall/8, 2*tileWall/8)
    line(5*tileWall/8, 3*tileWall/8, 5*tileWall/8, 5*tileWall/8)
    line(5*tileWall/8, 3*tileWall/8, 8*tileWall/8, 3*tileWall/8)
    line(6*tileWall/8, 4*tileWall/8, 8*tileWall/8, 4*tileWall/8)
    line(1*tileWall/8, 0*tileWall/8, 1*tileWall/8, 1*tileWall/8)
    line(1*tileWall/8, 1*tileWall/8, 0*tileWall/8, 1*tileWall/8)
    line(2*tileWall/8, 0*tileWall/8, 2*tileWall/8, 3*tileWall/8)
    line(0*tileWall/8, 3*tileWall/8, 2*tileWall/8, 3*tileWall/8)
    line(0*tileWall/8, 2*tileWall/8, 1*tileWall/8, 2*tileWall/8)
    line(3*tileWall/8, 3*tileWall/8, 3*tileWall/8, 0*tileWall/8)
    line(6*tileWall/8, 0*tileWall/8, 8*tileWall/8, 0*tileWall/8)
    line(8*tileWall/8, 1*tileWall/8, 6*tileWall/8, 1*tileWall/8)
    
def createTile5(tileWall):
    line(8*tileWall/8, 0*tileWall/8, 0*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    line(3*tileWall/8, 5*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    line(7*tileWall/8, 7*tileWall/8, 2*tileWall/8, 6*tileWall/8)
    line(6*tileWall/8, 6*tileWall/8, 1*tileWall/8, 7*tileWall/8)
    line(5*tileWall/8, 5*tileWall/8, 0*tileWall/8, 8*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 5*tileWall/8, 5*tileWall/8)
    line(5*tileWall/8, 3*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    line(6*tileWall/8, 2*tileWall/8, 7*tileWall/8, 7*tileWall/8)
    line(7*tileWall/8, 1*tileWall/8, 6*tileWall/8, 6*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 5*tileWall/8, 3*tileWall/8)
    line(6*tileWall/8, 2*tileWall/8, 1*tileWall/8, 1*tileWall/8)
    line(7*tileWall/8, 1*tileWall/8, 2*tileWall/8, 2*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 3*tileWall/8, 3*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 3*tileWall/8, 5*tileWall/8)
    line(1*tileWall/8, 1*tileWall/8, 2*tileWall/8, 6*tileWall/8)
    line(2*tileWall/8, 2*tileWall/8, 1*tileWall/8, 7*tileWall/8)
    line(3*tileWall/8, 3*tileWall/8, 0*tileWall/8, 8*tileWall/8)

def createTile6(tileWall):
    line(0*tileWall/8, 0*tileWall/8, 1*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 1*tileWall/8, 2*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 2*tileWall/8, 3*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 3*tileWall/8, 4*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 4*tileWall/8, 5*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 5*tileWall/8, 6*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 6*tileWall/8, 7*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 7*tileWall/8, 8*tileWall/8, 8*tileWall/8)

def createTile7(tileWall):
    line(0*tileWall/8, 0*tileWall/8, 1*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 1*tileWall/8, 2*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 2*tileWall/8, 3*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 3*tileWall/8, 4*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 4*tileWall/8, 5*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 5*tileWall/8, 6*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 6*tileWall/8, 7*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 7*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 8*tileWall/8, 1*tileWall/8)
    line(1*tileWall/8, 0*tileWall/8, 8*tileWall/8, 2*tileWall/8)
    line(2*tileWall/8, 0*tileWall/8, 8*tileWall/8, 3*tileWall/8)
    line(3*tileWall/8, 0*tileWall/8, 8*tileWall/8, 4*tileWall/8)
    line(4*tileWall/8, 0*tileWall/8, 8*tileWall/8, 5*tileWall/8)
    line(5*tileWall/8, 0*tileWall/8, 8*tileWall/8, 6*tileWall/8)
    line(6*tileWall/8, 0*tileWall/8, 8*tileWall/8, 7*tileWall/8)
    line(7*tileWall/8, 0*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    
