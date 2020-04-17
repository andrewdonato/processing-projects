import math

def setup():
    size(500,500, P3D)
    
    
def draw():
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
                    
    
    if mouseX > 0 and mouseY > 0 : 
        
        translate(width/2,height/2,-400 + mouseY*1.6)
        # translate(width/2,height/2,-400 + mouseHypotenuse*1.13)
        
    else:
        translate(width/2,height/2, -400)
    stroke(0)
    sphere(height/10)

    popMatrix()




## math
# mouseHypotenuse = math.sqrt(mouseX**2 + mouseY**2) 
# totalHypotenuse = math.sqrt(width**2 + height**2)

# -400 .. 400 == 800  ## this is the depth range the sphere is covering
# 800 * 100/500 == 160

# print totalHypotenuse    ## 707.106781187 for 500*500 screen
# print 800 * 100/707.1 ## 113.13816999
