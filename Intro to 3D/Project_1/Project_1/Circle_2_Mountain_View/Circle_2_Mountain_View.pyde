#Armontae Harris 02/14/2021
#Mountain View

import os
from PolyLine import PolyLine

#Global Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

Radius = Width/3


x1 = []
y1 = []
z1 = []

HorAngle = 0
VerAngle = 0

file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(0,0,0)
    smooth(100)

def draw():
    background(40, 40, 100)
    
    global CenterX,CenterY, Width, Height, Radius, HorAngle, x1,y1,z1
    translate(CenterX,CenterY)
    
    HorAngle += 2  
    
    # calculating the points on a circle
    x =  cos(radians(HorAngle*HorAngle))* Radius 
    y =  -1 * sin(radians(HorAngle/x * 5))* Radius
    
    x1.append(x)
    y1.append(y)
    z1.append(0)
    
    strokeWeight(.75)
    
    PolyLine(x1,y1,z1)
    
    strokeWeight(.5)
    stroke(165,120,120)
    line(0,0,x,y)
    line(0,0,x,0)
    line(x,y,x,0)
    
    textSize(20)
    fill(255)
    
    x2 = int(x)
    y2 = int(y)
    text(str((x2,y2)),x,y)
    

    

    
    
    
    #condition to end drawing and save image
    if HorAngle >= 360*4:
            save(str("images/" + str(file_name) + str(minute))+ ".jpg")       
        
            noLoop()
    
