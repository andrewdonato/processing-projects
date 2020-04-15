# Display a 200x200 pixel image, pixel by pixel. 
def setup():
    global img

    size(200, 200)
    img = loadImage("tenor.gif") #should be 498,249, but im using a smaller screen
    


def draw():

    loadPixels()
    # Since we are going to access the image's pixels too  
    img.loadPixels()
    for y in xrange(height):
        for x in xrange(width):
            
            loc = x + y*width
            imageLoc = displayLoc = loc
            
            # The functions red(), green(), and blue() pull out the 
            # 3 color components from a pixel.
            r = red(img.pixels[imageLoc])
            g = green(img.pixels[imageLoc])
            b = blue(img.pixels[imageLoc])
            # print "%s, %s, %s," %(r,g,b)
            # Image Processing would go here
            # If we were to change the RGB values, we would do it here, 
            # before setting the pixel in the display window.
      
            # Set the display pixel to the image pixel
            pixels[displayLoc] =  color(r,g,b)
                

    updatePixels()
