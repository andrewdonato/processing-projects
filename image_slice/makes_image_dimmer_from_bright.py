# Display a 200x200 pixel image, pixel by pixel. 
def setup():
    global img

    # size(498,249)
    # img = loadImage("tenor.gif")
    
    size(200, 200)
    img = loadImage("sunflower.jpg")
    
    
    


def draw():

    loadPixels()
    # Since we are going to access the image's pixels too  
    img.loadPixels()
    
    for x in xrange(img.width):
        for y in xrange(img.height):
            # Calculate the 1D pixel location
            loc = x + y*img.width
            # Get the R,G,B values from image
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            
            # Change brightness according to the mouse here
            # adjustBrightness = ((float) mouseX / width) * 8.0
            # adjustBrightness = float((mouseX / width) * 255.0)
            # adjustBrightness = float((mouseX / width) * 10.0)
            # adjustBrightness = float(mouseX / width) * 100.0
            # adjustBrightness = float(mouseX/width)*8.0
            
            if mouseX > 0:
                adjustBrightness = float(width/mouseX)
                # adjustBrightness = (mouseX)
            else:
                adjustBrightness = float(mouseX)
            r *= adjustBrightness
            g *= adjustBrightness
            b *= adjustBrightness
            
            # r += adjustBrightness
            # g += adjustBrightness
            # b += adjustBrightness
        
            
            # Constrain RGB to between 0-255
            r = constrain(r,0,255)
            g = constrain(g,0,255)
            b = constrain(b,0,255)
            # Make a new color and set pixel in the window
            c = color(r,g,b)
            pixels[loc] = c
    
                    

    updatePixels()
