from tiles import *

tileWall = 60
speed = 2
drawTile = createTile15

def setup():
    size(1201,601)
    background(255)

    
def draw():
    # noCursor()
    frameRate(speed)
    background(255)
    placeTiles()
    
    # rect(0,0,3*tileWall,3*tileWall)
    # translate(tileWall,tileWall)
    # scale(-1,1);
    # translate(-tileWall,)
    # createTile3(tileWall)
      

def placeTiles():        
    for y in range(0, height, tileWall):
        for x in range(0, width, tileWall):
            pushMatrix()
            
            translate(x, y)
            
            ## flip
            flipChance = int(random(0,2))                    
            if flipChance == 1:
                scale(-1,1);
                translate(-tileWall,0)   

                                             
            ## rotation                                                                              
            turns = int(random(0, 4))
            rotation = turns * 90                            
            rotate(radians(rotation))                                                                                                                                                                        
            if rotation == 90:
                translate(0, -tileWall)
            elif rotation == 180:
                translate(-tileWall, -tileWall)
            elif rotation == 270 :
                translate(-tileWall, 0)                                           
            
            strokeWeight(1)
            noFill()
            # stroke(200)
            # rect(0,0,tileWall,tileWall)
            stroke(0)
            drawTile(tileWall)
                
            popMatrix()
    
def keyReleased():
    global tileWall, speed
    # if key == "a" or key == "A" :
    
    # if key == " " :
    #     background(255)
    #     placeTiles()

    if key == "=" or key == "+" :      
        tileWall += 10
    elif key == "-" or key == "_" :
        if tileWall > 10 :      
            tileWall -= 10

    if key == "[" or key == "{" :
        noLoop()
        
    #     if speed > 0:
    #         speed = 0
    elif key == "]" or key == "}" :
        redraw()
    elif key == "\\" or key == "|" :
        loop()
    #     if speed < 60:
    #         speed = 1
        

                
        


                                          
                        
                                                
