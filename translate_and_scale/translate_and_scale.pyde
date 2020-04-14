def setup():
    size (500, 500)
    background (255)
    
    # strokeWeight = 10
    line(0,50, width,50)
    stroke(255,0,0)
    
    line(width*.5, height*.9, width*.5, height*.1)
    # stroke(0,255,0)
    line(250, 450, 250, 50)
    stroke(0)
    # translate(40, -60)
    translate(40, 0)
    # scale(1.2)
    # line(250, 450, 250, 50)
    # line(width*.5, height*.9, width*.5, height*.1)
    # line(width*.6, height*.5, width*.6, height*.1)
    
    
def draw():
    print(mouseX, mouseY)
    
    # scale(1*250/mouseX)
    if mouseX > 0 and mouseX < width:
        print float(1*250/mouseX)    
          # width/2 = 1
    
