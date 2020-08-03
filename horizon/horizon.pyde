xMax = 5500
yMax = 500
zMax = 5500
diff = 0

def setup():    
    frameRate(1)
    size(500,500, P3D)
    stroke(0)
    strokeWeight(0.5)
    background(255)
    
def draw():
    global diff
    background(255)
    drawGrid()
    pushMatrix()
    translate(0, yMax, 0)
    drawGrid()
    popMatrix()
    
    ## rotating line
    # if diff <= width:
    #     diff += width/10
    # else:
    #     diff = 0
    # line(diff,0,0,width-diff,height,0)
    
    
    # translate(100,100,0)
    # stroke(0)
    # box(100,100,100)
    # stroke(255,0,0)
    # pushMatrix()
    
    # translate(0,0,100)
    # box(100,100,2)
    # popMatrix()
    # camera(3 * mouseX - width, 2 * mouseY - height, 1 * (height / 2.0) / tan(PI * 30.0 / 180.0),
    # width / 2.0, height / 10.0, height / 2, 0, 1, 0)
        
def drawGrid():
    x = -2*xMax
    
    while x < 2*xMax :
        
        # line(x, 0, 0, xMax, 0, zMax)
        line(x, 0, -zMax, x, 0, zMax)
        x = x + 50
    
    # z = -zMax
    
    # while z < zMax/1000 :
        
    #     # line(x, 0, 0, xMax, 0, zMax)
    #     line(-xMax, 0, z, xMax, 0, z)
    #     z += 50
    
