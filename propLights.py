#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel

DATA = "D18"
raygunPixels = 6
shipPixels = 7
cryopodPixels = 2
 

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
#pixels1 = neopixel.NeoPixel(board.D18, 6, brightness=1)

pixels1 = neopixel.NeoPixel(board.D18,raygunPixels, brightness=.3)
raygun = neopixel.NeoPixel(board.D18,raygunPixels, brightness=.3)
ship = neopixel.NeoPixel(board.D18,shipPixels, brightness=.3)
cryopod = neopixel.NeoPixel(board.D18,shipPixels, brightness=.3)

#Also create an arbitrary count variable
x=0

#Focusing on a particular strip, use the command Fill to make it all a single colour
#based on decimal code R, G, B. Number can be anything from 255 - 0. Use an RGB Colour
#Code Chart Website to quickly identify the desired fill colour.


#Color Fades

sideA = [0, 2, 4]
sideB = [1, 3, 5]

def raygun_ShootVibe():
    dark = (50, 0, 50)
    light = (200, 0, 200)

    steps = 50  # smoothness of fade

    # Move the pulse along the 3 positions
    for pos in range(3):  # 0→1→2
        for i in range(steps):
            # interpolation factor 0→1
            t = i / steps

            # compute fade color
            r = int(dark[0] + (light[0] - dark[0]) * t)
            g = 0
            b = int(dark[2] + (light[2] - dark[2]) * t)
            color = (r, g, b)

            # reset all pixels to dark
            raygun.fill(dark)

            # brighten the current pair
            raygun[sideA[pos]] = color
            raygun[sideB[pos]] = color

            raygun.show()
            time.sleep(0.001)

        # fade back down
        for i in range(steps):
            t = i / steps
            r = int(light[0] - (light[0] - dark[0]) * t)
            b = int(light[2] - (light[2] - dark[2]) * t)
            color = (r, 0, b)

            raygun.fill(dark)
            raygun[sideA[pos]] = color
            raygun[sideB[pos]] = color

            raygun.show()
            time.sleep(0.001)

def raygun_Shoot():
    dark = (50, 0, 50)
    light = (200, 0, 200)
    

    # Fade to light
    for i in range(100):
        # Linearly interpolate between dark and light
        # (Simplified example)
        raygun.fill((int(50 + (i*1.5)), 0, int(50 + (i*1.5))))
        raygun.show()
        time.sleep(0.02)
        
    # Fade to dark
    for i in range(100):
        raygun.fill((int(200 - (i*1.5)), 0, int(200 - (i*1.5))))
        raygun.show()
        time.sleep(0.02)



#RAYGUN PROP PIXEL FUNCTIONS 

def raygun_NoPower():
  
  x=0

  pixelBrightness=0

  while x < 5:
    while pixelBrightness <= .3:
      raygun[0] = (0,255, 255)
      raygun[1] = (0,255, 255)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)
    
    time.sleep(.01)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,255, 255)
      raygun[3] = (0,255, 255)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)

    time.sleep(.01)
    pixelBrightness=.05

    x=x+1

  x=0 #second phase

  while x < 5:
    while pixelBrightness <= .3:
      raygun[0] = (0,255, 255)
      raygun[1] = (0,255, 255)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)
    
    time.sleep(.005)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,255, 255)
      raygun[3] = (0,255, 255)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)

    time.sleep(.005)
    pixelBrightness=.05

    x=x+1  

  x=0 #third phase

  while x < 5:
    while pixelBrightness <= .3:
      raygun[0] = (0,255, 255)
      raygun[1] = (0,255, 255)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun[4] = (0,0,0)
      raygun[5] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .05
      raygun.show()
      time.sleep(.005)
    
    time.sleep(.0005)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,255, 255)
      raygun[3] = (0,255, 255)
      raygun[4] = (0,0,0)
      raygun[5] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .05
      raygun.show()
      time.sleep(.005)

    time.sleep(.0005)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun[4] = (0,255, 255)
      raygun[5] = (0,255, 255)
      raygun.brightness=pixelBrightness
      pixelBrightness += .05
      raygun.show()
      time.sleep(.005)

    time.sleep(.0005)
    pixelBrightness=.05

    x=x+1  

  raygun.fill((255, 255, 255))
  raygun.show()

  x=0 #4th phase

  while x < 2:
    pixelBrightness=.3
    while pixelBrightness >= 0:
      raygun.fill((255, 255, 255))

      raygun.brightness=pixelBrightness
      pixelBrightness -= .01
      raygun.show()
      time.sleep(.01)

      raygun.fill((255, 255, 255))
      raygun.show()

    raygun.fill((0, 0, 0))
    raygun.show()

    time.sleep(.1)

    x=x+1

  x=0 #final phase

  while x < 3:
    raygun.fill((255, 0, 0))
    raygun.show()

    pixelBrightness=.3
    while pixelBrightness >= 0:
      raygun.fill((255, 0, 0))

      raygun.brightness=pixelBrightness
      pixelBrightness -= .001
      raygun.show()
      time.sleep(.001)  

    x=x+1 

  raygun.fill((0,0,0))
  raygun.show()

def raygun_Power(): 
  
  x=0

  pixelBrightness=0

  while x < 5:
    while pixelBrightness <= .3:
      raygun[0] = (0,255, 255)
      raygun[1] = (0,255, 255)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)
    
    time.sleep(.01)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,255, 255)
      raygun[3] = (0,255, 255)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)

    time.sleep(.01)
    pixelBrightness=.05

    x=x+1

  x=0 #second phase

  while x < 5:
    while pixelBrightness <= .3:
      raygun[0] = (0,255, 255)
      raygun[1] = (0,255, 255)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)
    
    time.sleep(.005)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,255, 255)
      raygun[3] = (0,255, 255)
      raygun.brightness=pixelBrightness
      pixelBrightness += .025
      raygun.show()
      time.sleep(.005)

    time.sleep(.005)
    pixelBrightness=.05

    x=x+1  

  x=0 #third phase

  while x < 5:
    while pixelBrightness <= .3:
      raygun[0] = (0,255, 255)
      raygun[1] = (0,255, 255)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun[4] = (0,0,0)
      raygun[5] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .05
      raygun.show()
      time.sleep(.005)
    
    time.sleep(.0005)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,255, 255)
      raygun[3] = (0,255, 255)
      raygun[4] = (0,0,0)
      raygun[5] = (0,0,0)
      raygun.brightness=pixelBrightness
      pixelBrightness += .05
      raygun.show()
      time.sleep(.005)

    time.sleep(.0005)
    pixelBrightness=.05

    while pixelBrightness <= .3:
      raygun[0] = (0,0,0)
      raygun[1] = (0,0,0)
      raygun[2] = (0,0,0)
      raygun[3] = (0,0,0)
      raygun[4] = (0,255, 255)
      raygun[5] = (0,255, 255)
      raygun.brightness=pixelBrightness
      pixelBrightness += .05
      raygun.show()
      time.sleep(.005)

    time.sleep(.0005)
    pixelBrightness=.05

    x=x+1  

  raygun.fill((255, 255, 255))
  raygun.show()

  x=0 #4th phase

  while x < 2:
    pixelBrightness=.3
    #raygun_Shoot()

    x= x+1

  x=0 #4th phase

  while x < 10:
    pixelBrightness=.3
    raygun_ShootVibe()

    x= x+1

  raygun.fill((0,0,0))
  raygun.show()

  



#raygun_NoPower()
raygun_Power()

#Below demonstrates how to individual address a colour to a LED Node, in this case
#LED Node 10 and colour Blue was selected
#pixels1[10] = (0, 20, 255)

#Sleep for three seconds, You should now have all LEDs showing light with the first node
#Showing a different colour

#Little Light slider script, will produce a nice loading bar effect that goes all the way up a small Strip 
#and then all the way back
#This was created using a While Loop taking advantage of that arbitrary variable to determine
#which LED Node we will target/index with a different colour

#Below will loop until variable x has a value of 35
#while x<35:
    
    #pixels1[x] = (255, 0, 0)
    #pixels1[x-5] = (255, 0, 100)
    #pixels1[x-10] = (0, 0, 255)
    #Add 1 to the counter
    #x=x+1
    #Add a small time pause which will translate to 'smoothly' changing colour
    #time.sleep(0.05)

#Below section is the same process as the above loop just in reverse
#while x>-15:
    #pixels1[x] = (255, 0, 0)
    #pixels1[x+5] = (255, 0, 100)
    #pixels1[x+10] = (0, 255, 0)
    #x=x-1
    #time.sleep(0.05)

#Add a brief time delay to appreciate what has happened    


#Complete the script by returning all the LED to off
raygun.fill((0, 0, 0))
