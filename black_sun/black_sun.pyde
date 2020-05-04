## https://www.mathsisfun.com/numbers/nature-golden-ratio-fibonacci.html


def setup():
    size(500,500)
    background(0)
    
    stroke(255)
    strokeWeight(1)
    
    pushMatrix()
    translate(width/2, height/2)
        
    fill(0)    
    # ellipse(width/2, height/2, 100, 100)
    ellipse(0, 0, 100, 100)
    
    noFill()
    rectMode(CENTER)

    x = 6
    for i in range(0,x):
        
        goldenAngle = radians(137.5)
        # goldenTurns = radians(222.5)
        
        rotate(PI/goldenAngle)
        
        rect(0, 0, 100, 100)
        
    popMatrix()
        
        
        
        
    # rotate(.618)
    # rotate(PI/1.61803)
    
    
    # rect(0, 0, 100, 100)
    # rotate(PI/3.0)
    # rect(0, 0, 100, 100)
    # rotate(PI/3.0)
    # rect(0, 0, 100, 100)
    
    # rotate(PI/2.4)
    # rect(0, 0, 100, 100)
    # rotate(PI/3.0)
    # rect(0, 0, 100, 100)
    # rotate(PI/3.0)
    # rect(0, 0, 100, 100)
    
    
    
    
