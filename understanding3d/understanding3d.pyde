import math

depthRange=[]

def setup():
    global depthRange
    # size(500,500, P3D)
    size(700,700, P3D)
    # size(800,800, P3D)
    depthRange = [-(height*.8),(height*.8)]
    
def draw():
    moveCamera()
    global depthRange
    print (mouseX, mouseY)
    background(255)
    # stroke(255,0,0)    
    strokeWeight(1)
    pushMatrix()
    for y in range(0, height, height/10):
        for z in range(-400, height, height/10):
            for x in range(0, width, width/10):
                if x != width/2 and y != height/2:
                    stroke(x,0,0, z)
                    line(x, y, z, width, y, z)
                    stroke(0, y,0, z)
                    line(x, y, z, x, height, z)
                    stroke(0,0,z, 100)
                    strokeWeight(1)
                    line(x, y, z, x, y, height)
                    fill(0)
                    
    totalDepthRange = abs(depthRange[0]-depthRange[1])
    # sphereMouseRatio = float(totalDepthRange/height)
    sphereMouseRatio = float(totalDepthRange*100/height)
    # print float (sphereMouseRatio/100)
    print totalDepthRange
    print sphereMouseRatio
    if mouseX > 0 and mouseY > 0 : 
        
        translate(width/2,height/2, depthRange[0] + mouseY*sphereMouseRatio/100)
        # translate(width/2,height/2, depthRange[0] + mouseY*1.6)
        # translate(width/2,height/2,-400 + mouseHypotenuse*1.13)
        
    else:
        translate(width/2,height/2, depthRange[0])
    stroke(0)
    sphere(height/10)

    popMatrix()

def moveCamera():
    # camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0)
    cameraAngle = (width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0, 1, 0)
    if key == CODED:
        if keyCode == LEFT:
            cameraAngle = (width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, -0.5, 1.0, 0)
        elif keyCode == RIGHT:
            cameraAngle = (width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), width/2.0, height/2.0, 0, 0.5, 1, 0)    
    camera(*cameraAngle)
    





## math
# mouseHypotenuse = math.sqrt(mouseX**2 + mouseY**2) 
# totalHypotenuse = math.sqrt(width**2 + height**2)

# -400 .. 400 == 800  ## this is the depth range the sphere is covering
# 800 * 100/500 == 160

# print totalHypotenuse    ## 707.106781187 for 500*500 screen
# print 800 * 100/707.1 ## 113.13816999
