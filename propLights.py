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

#RAYGUN PROP PIXEL FUNCTIONS 

def raygun_NoPower():
  
  x=0

  while x < 15:
    raygun[(1,2)] = (0,255, 255)
    time.sleep(0.05)
    raygun[(1,2)] = (0,0,0)
    raygun[(3,4)] = (0,255, 255)
    time.sleep(0.05)
    raygun[(3,4)] = (0,0,0)
    #pixels1[x+5] = (255, 0, 100)
    #pixels1[x+10] = (0, 255, 0)
    x=x+1
    #time.sleep(0.05)

raygun_NoPower()

raygun.fill((0, 255, 255))

#Below demonstrates how to individual address a colour to a LED Node, in this case
#LED Node 10 and colour Blue was selected
#pixels1[10] = (0, 20, 255)

#Sleep for three seconds, You should now have all LEDs showing light with the first node
#Showing a different colour
time.sleep(10)

raygun.fill((0, 0, 0))

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
time.sleep(4)

#Complete the script by returning all the LED to off
raygun.fill((0, 0, 0))
