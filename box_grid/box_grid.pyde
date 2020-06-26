boardSize = 1000
boxSize = 50
marginSize = 20

def setup():    
    size(700,700, P3D)
    background(255)
    noFill()
    # camera(3*mouseX - 2*width, 3*mouseY - 2*height, 2*(height/2.0) / tan(PI*30.0 / 180.0), width/2.0, -height/10.0, -height/2, 0, 1, 0)
    # camera(width/2.0, -height/10.0, -height/2, 3*mouseX - 2*width, 3*mouseY - 2*height, 2*(height/2.0) / tan(PI*30.0 / 180.0),  0, 1, 0)
    
    # normal camera
    # camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0)    
    
def draw():
    background(255)
    
    # translate(boardSize/2, boardSize/2, boardSize/2)
    # translate(width/2.0, -height/10.0, -height/2)
    
    anchorBox()
    boxGrid()
    # camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0)  # centered, no movement
    # camera(width/4.0, height/4.0, (height/1.5) / tan(PI*30.0 / 180.0), 3*mouseX - width/4.0, 3*mouseY-height/4.0, 0, 0, 1, 0)
    # camera(width/4.0, height/4.0, (height/1.5) / tan(PI*30.0 / 180.0), 3*mouseX - width/4.0, 3*mouseY-height/4.0, -(height/2.0) / tan(PI*30.0 / 180.0), 0, 1, 0)
    
    # camera(width/2.0, -height/10.0, -height/2, 3*mouseX - 2*width, 3*mouseY - 2*height, 2*(height/2.0) / tan(PI*30.0 / 180.0),  0, 1, 0)  #moves anchorBox to the top/front/left
    camera(3*mouseX - 2*width, 3*mouseY - 2*height, 2*(height/2.0) / tan(PI*30.0 / 180.0), width/2.0, -height/10.0, -height/2, 0, 1, 0)  #distant view, box on top/back/left

def anchorBox():
    pushMatrix()        
    # translate(x, y, z)
    fill(255, 0 , 0)
    box(boxSize - marginSize)
    noFill()        
    popMatrix()        
    
            
def boxGrid():

    for x in range(0, boardSize, boxSize):
        for y in range(0, boardSize, boxSize):
            for z in range(0, boardSize, boxSize):
                pushMatrix()        
                translate(x, y, z)
                # fill(250)
                box(boxSize - marginSize)        
                popMatrix()        
    
                
    
    
    # x = 0
    # while x < boardSize :
    #     pushMatrix()        
    #     translate(x, 0, 0)
    #     box(boxSize)        
    #     popMatrix()
        
    #     pushMatrix()        
    #     translate(0, x, 0)
    #     box(boxSize)        
    #     popMatrix()
        
    #     pushMatrix()        
    #     translate(0, 0, x)
    #     box(boxSize)        
    #     popMatrix()
        
        
    #     x += boxSize
        
