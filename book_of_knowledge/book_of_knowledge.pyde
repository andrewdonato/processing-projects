def setup():
    size(700,700,P3D)
    background(255)
    
def draw():
    camera(3*mouseX - 2*width, 3*mouseY - 2*height, 1*(height/2.0) / tan(PI*30.0 / 180.0), width/2.0, -height/10.0, -height/2, 0, 1, 0)  #distant view, box on top/back/left
    background(255)
    
    # red anchor
    stroke(155,0,0)
    noFill()
    box(100,100,100)
    
    # green anchor
    pushMatrix()
    translate(100,0,0)
    stroke(0,155,0)
    box(100,100,100)
    popMatrix()
    
    
    translate(width/2, height/2, 0)
    
    # blue book
    pushMatrix()
    stroke(0,150,226)
    fill(28,181,226)
    box(200,300,20)
    popMatrix()
    
    # cover
    translate(-30,0,80)
    rotateY(-PI/4)
    # translate(30,0,80)
    
    stroke(155,0,0)
    fill(155,0,0)
    box(200,300,2)
    
    # green square
    pushMatrix()
    translate(0,0,2)
    stroke(0,155,0)
    fill(0,155,0)
    box(50,50,1)
    popMatrix()
    
