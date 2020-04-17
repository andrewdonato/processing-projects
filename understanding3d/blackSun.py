def setup():
    size(700,700, P3D)
    background(255)
    
def draw():
    # stroke(255,0,0)    
    strokeWeight(1)
    for y in range(0, height, height/10):
        for z in range(0, height, height/10):
            for x in range(0, width, width/10):
                # line(x, y, z, width, y, z)
                # line(x, y, z, x, height, z)
                line(x, y, z, x, y, height)
                fill(0)
                # circle(width/2,height/2, height/6)
                circle(width/2,height/2, height/10)
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
    
    
    
