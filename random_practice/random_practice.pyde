size(500,500)

# # random
for i in range(0, height):
    r = int(random(500))
    # r = randomGaussian()
    print r
    stroke(r*5/10)
    line(50, i, 50+r, i )
    
    
# # noise detail
# noiseVal = 0
# noiseScale = 0.02

# for y in range(height):
#   for x in range(width / 2):
#     noiseDetail(3, 0.5)
#     noiseVal = noise(
#         x * noiseScale, y * noiseScale)
#     stroke(noiseVal * 255)
#     point(x, y)
#     noiseDetail(8, 0.65)
#     noiseVal = noise((x + width/2) * noiseScale,
#                      y * noiseScale)
#     stroke(noiseVal * 255)
#     point(x + width/2, y)



# # noise
# xoff = 0.0
# background(204)
# for i in range(1000):
#   xoff = xoff + .01
#   n = noise(xoff) * width
#   line(n, 0, n, height)
  
# noiseScale = 0.02
# def draw():
#     background(0)
#     for x in range(width):
#         noiseVal = noise((mouseX + x) * noiseScale, mouseY * noiseScale)
#         stroke(noiseVal * 255)
#         line(x, mouseY + noiseVal * 80, x, height)
