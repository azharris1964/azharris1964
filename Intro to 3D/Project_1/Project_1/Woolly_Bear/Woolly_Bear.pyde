#Armontae Harris
#Woolly Bear
#2.17.21

import os
from PolyLine import PolyLine
from TrigCirc import TrigCirc
from Triangle import Triangle

#Globale Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

Radius = Width/5

MakeMovie = False

#Global Variables

HorAngle = 0
HorAngle2 = 0
HorAngle3 = 0

Add = 0
CouVerAngle = 0

X1 = []
Y1 = []
Z1 = []

Rotation = 0

file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    smooth(100)
    

def draw():
    background(50,150,50)
    global CenterX, CenterY, Radius,X1,Y1,Z1,Rotation
    #Add change to global horizontal angle
    
    #Grow the number of rotations
    
    Rotation += 1
    
    
    
    
    translate(CenterX,CenterY)
    

    
    #find point on circle
    stroke(0)
    strokeWeight(1)
    CircPoints = TrigCirc(205,2,Radius,Rotation,0,0,0,"Oblique")
    
    x= CircPoints[0]
    y= CircPoints[1]
    z= CircPoints[2]
    

    stroke(0)
    strokeWeight(.75)
    PolyLine(X1,Y1,Z1)
    
    #draw triangle
    stroke(50)
    strokeWeight(.5)
    Triangle(0,0,0,x,y,z)

    
    #add text to point
    
    textSize(10)
    fill(0)
    noFill()
  
    
    

    if MakeMovie == True:
        saveFrame("anim/" + "frame" + "-####.png")
    
    


    
