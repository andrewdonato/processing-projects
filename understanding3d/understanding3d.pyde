def setup():
    size(500,500, P3D)
    
    
def draw():
    print (mouseX, mouseY)
    background(255)
    # stroke(255,0,0)    
    strokeWeight(1)
    for y in range(0, height, height/10):
        for z in range(0, height, height/10):
            for x in range(0, width, width/10):
                if x != width/2 and y != height/2:
                    stroke(x,0,0, 50)
                    line(x, y, z, width, y, z)
                    stroke(0, y,0, 50)
                    line(x, y, z, x, height, z)
                    stroke(0,0,z, 50)
                    strokeWeight(1)
                    line(x, y, z, x, y, height)
                    fill(0)
                    # circle(width/2,height/2, height/6)
                    stroke(0)

    # circle(width/2,height/2, height/10)                
    # translate(width/2,height/2,414)
    
    if mouseX > 0 and mouseY > 0 : 
        translate(width/2,height/2,-400 + mouseY*1.6)
        # sphereDetail(360)
        # sphere(height/mouseY)
    else:
        translate(width/2,height/2, -400)
    sphere(height/10)

    # popMatrix()

    # translate(width/2,height/2, 390)
    # box(10,10,1)
        
        
        
    # for j in range(0, height, height/10):
    #     # line(0, j, 0, width, j, 0)
    
    #     stroke(0,0,255)
    #     for i in range(0, width, width/10):
    #         #ine(x, y, z, x,     y, z)
    #         line(i, j, 0, i, height, 0)
        
        
            
    #     stroke(0,255,0)
    #     for k in range(0, height, height/10):
    #         line(0, (height/2)+100, k, width, (height/2)+100, k)
        
    
    # stroke(0,255,0)
    # for i in range(0, width, width/10):
    #     #ine(x, y, z, x,     y, z)
    #     line(i, 0, 0, i, height, 0)
    
    # stroke(255,0,0)    
    # for j in range(0, height, height/10):
    #     line(0, j, 0, width, j, 0)
    # stroke(0,0,255)    
    # for k in range(0, height, height/10):
    #     line(0, (height/2)+100, k, width, (height/2)+100, k)
    
    
    
