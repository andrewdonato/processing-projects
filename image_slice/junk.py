# def setup():
#   global img
#   # size(320,240)
#   # size(500,1000)
#   size(900,1121)
#   # Make a new instance of a PImage by loading an image file
#   # Declaring a variable of type PImage
#   # img = loadImage("mysummervacation.jpg")
#   back = loadImage("newlandscape6_stars.jpg")  # 900 x 1121
#   # back = loadImage("international-andrew.jpg")
#   background(back)
# # img = loadImage("m-c-escher-ascending-and-descending.jpg")
#   img = loadImage("optical-illusion-illusion-art-abstract-twisted-black-and-white-background-vector-illustration-.jpg")
#   print type(img)
# cyber-punk-diorama.jpg #404 x 533

# # def draw():
#   global img
#   # background(255);
#   # Draw the image to the screen at coordinate (0,0)
#   # image(img,-300,-20)
#   tint(0,0,255,50)
#   image(img, -10, 0, 500, 500*1.2456)
  
#   tint(0,255,0,50)
#   image(img, 0, 0, 500, 500*1.2456)
  
#   tint(255,0,0,50)
#   image(img, 10, 0, 500, 500*1.2456)
  
  
img = createImage(320,240,RGB) # Make a PImage object
print(img.width)  # Yields 320
print(img.height) # Yields 240
img.pixels[0] = color(255,0,0)  # Sets the first pixel of the image to red

# Display a 200x200 pixel image, pixel by pixel. 
def setup():
    global img
    # size(200, 200)
    size(900, 1000)
    img = loadImage("cyber-punk-diorama.jpg")


def draw():
    loadPixels()
    # Since we are going to access the image's pixels too  
    img.loadPixels()
    
    # for y in xrange(height):
    #     for x in xrange(width):
    #         loc = x + y*width
      
    #         # The functions red(), green(), and blue() pull out the 
    #         # 3 color components from a pixel.
    #         r = red(img.pixels[loc])
    #         g = green(img.pixels[loc])
    #         b = blue(img.pixels[loc])
      
    #         # Image Processing would go here
    #         # If we were to change the RGB values, we would do it here, 
    #         # before setting the pixel in the display window.
      
    #         # Set the display pixel to the image pixel
    #         pixels[loc] =  color(r,g,b)        
    
    # for x in xrange(img.width):
    #     for y in xrange(img.height):
    #         # Calculate the 1D pixel location
    #         loc = x + y*img.width
    #         # Get the R,G,B values from image
    #         r = red(img.pixels[loc])
    #         g = green(img.pixels[loc])
    #         b = blue(img.pixels[loc])
            
    #         # Change brightness according to the mouse here
    #         adjustBrightness = float((mouseX / width) * 8.0)
    #         r *= adjustBrightness
    #         g *= adjustBrightness
    #         b *= adjustBrightness
        
    #         # Constrain RGB to between 0-255
    #         r = constrain(r,0,255)
    #         g = constrain(g,0,255)
    #         b = constrain(b,0,255)
    #         # Make a new color and set pixel in the window
    #         c = color(r,g,b)
    #         pixels[loc] = c


    updatePixels()
