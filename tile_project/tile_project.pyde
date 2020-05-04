def setup():
    size(601,601)
    
def draw():
    background(255)
    
    tileWidth = 60
    createTile(tileWidth)
    

def createTile(tileWidth):
    noFill()
    ## tile outline
    rect(0,0,tileWidth,tileWidth)
    ## inside circle
    arc(0,0,tileWidth/2,tileWidth/2, 0, HALF_PI)
    ## square star corner
    line(0, 3*tileWidth/4, tileWidth/4, tileWidth/2)
    line(tileWidth/4, tileWidth/2, tileWidth/2, tileWidth/2)
    line(tileWidth/2, tileWidth/2, tileWidth/2, tileWidth/4)
    line(3*tileWidth/4, 0, tileWidth/2, tileWidth/4)
    ## round star corner
    line(0, tileWidth, tileWidth/2, 3*tileWidth/4)
    arc(3*tileWidth/4, 3*tileWidth/4, tileWidth/2, tileWidth/2, PI, PI+HALF_PI)
    line(tileWidth, 0, 3*tileWidth/4, tileWidth/2)
    ## inside square
    line(3*tileWidth/4, tileWidth, 3*tileWidth/4, 3*tileWidth/4)
    line(tileWidth,3*tileWidth/4, 3*tileWidth/4, 3*tileWidth/4)
