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

def createTile8(tileWall):
    pass
    line(1*tileWall/8, 1*tileWall/8, 0*tileWall/8, 2*tileWall/8)
    line(1*tileWall/8, 1*tileWall/8, 2*tileWall/8, 2*tileWall/8)
    line(3*tileWall/8, 1*tileWall/8, 0*tileWall/8, 4*tileWall/8)
    line(3*tileWall/8, 1*tileWall/8, 4*tileWall/8, 2*tileWall/8)
    line(8*tileWall/8, 6*tileWall/8, 7*tileWall/8, 7*tileWall/8)
    line(7*tileWall/8, 7*tileWall/8, 6*tileWall/8, 6*tileWall/8)
    line(8*tileWall/8, 4*tileWall/8, 5*tileWall/8, 7*tileWall/8)
    line(5*tileWall/8, 7*tileWall/8, 4*tileWall/8, 6*tileWall/8)
    line(3*tileWall/8, 7*tileWall/8, 8*tileWall/8, 2*tileWall/8)
    line(0*tileWall/8, 6*tileWall/8, 5*tileWall/8, 1*tileWall/8)
    line(5*tileWall/8, 1*tileWall/8, 6*tileWall/8, 2*tileWall/8)
    line(3*tileWall/8, 7*tileWall/8, 2*tileWall/8, 6*tileWall/8)
    line(6*tileWall/8, 2*tileWall/8, 2*tileWall/8, 6*tileWall/8)
    line(2*tileWall/8, 6*tileWall/8, 0*tileWall/8, 8*tileWall/8)
    line(6*tileWall/8, 2*tileWall/8, 8*tileWall/8, 0*tileWall/8)
    
def createTile9(tileWall):
    pass
    line(0*tileWall/8, 0*tileWall/8, 1*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 2*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 3*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 4*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 5*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 6*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 7*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 1*tileWall/8, 1*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 2*tileWall/8, 2*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 3*tileWall/8, 3*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 4*tileWall/8, 4*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 5*tileWall/8, 5*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 6*tileWall/8, 6*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 7*tileWall/8, 7*tileWall/8)
    line(0*tileWall/8, 0*tileWall/8, 0*tileWall/8, 8*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 0*tileWall/8, 0*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    
def createTile10(tileWall):
    rect(0,0,tileWall, tileWall)
    line(1*tileWall/8, 0*tileWall/8, 1*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 4*tileWall/8, 4*tileWall/8, 4*tileWall/8)
    line(4*tileWall/8, 4*tileWall/8, 8*tileWall/8, 8*tileWall/8)
    line(2*tileWall/8, 0*tileWall/8, 2*tileWall/8, 8*tileWall/8)
    line(3*tileWall/8, 0*tileWall/8, 3*tileWall/8, 8*tileWall/8)
    line(0*tileWall/8, 5*tileWall/8, 3*tileWall/8, 5*tileWall/8)
    line(0*tileWall/8, 6*tileWall/8, 6*tileWall/8, 6*tileWall/8)
    line(0*tileWall/8, 7*tileWall/8, 3*tileWall/8, 7*tileWall/8)
    line(0*tileWall/8, 2*tileWall/8, 8*tileWall/8, 2*tileWall/8)
    line(4*tileWall/8, 2*tileWall/8, 8*tileWall/8, 6*tileWall/8)
    line(4*tileWall/8, 0*tileWall/8, 4*tileWall/8, 2*tileWall/8)
    line(5*tileWall/8, 2*tileWall/8, 8*tileWall/8, 5*tileWall/8)
    line(5*tileWall/8, 3*tileWall/8, 8*tileWall/8, 3*tileWall/8)
    line(6*tileWall/8, 4*tileWall/8, 8*tileWall/8, 4*tileWall/8)
    line(6*tileWall/8, 2*tileWall/8, 8*tileWall/8, 4*tileWall/8)
    line(4*tileWall/8, 1*tileWall/8, 1*tileWall/8, 1*tileWall/8)
    line(5*tileWall/8, 2*tileWall/8, 5*tileWall/8, 0*tileWall/8)
    line(6*tileWall/8, 2*tileWall/8, 6*tileWall/8, 0*tileWall/8)
    line(5*tileWall/8, 1*tileWall/8, 8*tileWall/8, 1*tileWall/8)
    line(5*tileWall/8, 3*tileWall/8, 4*tileWall/8, 4*tileWall/8)

def createTile11(tileWall):
    line(3*tileWall/8, 1*tileWall/8, 2*tileWall/8, 2*tileWall/8)
    line(4*tileWall/8, 1*tileWall/8, 2*tileWall/8, 3*tileWall/8)
    line(5*tileWall/8, 1*tileWall/8, 2*tileWall/8, 4*tileWall/8)
    line(7*tileWall/8, 0*tileWall/8, 1*tileWall/8, 6*tileWall/8)
    line(8*tileWall/8, 0*tileWall/8, 0*tileWall/8, 8*tileWall/8)
    
