#Armontae Harris
#03/02/2021
#Draws object with while loop

#import classes
import rhinoscriptsyntax as rs
import math

#modules
import Spherical 
import CaptureView

#import function
from Spherical import TrigCirc
from CaptureView import GetCaptureView

#refresh
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

#Reloads custom files
from imp import reload
reload(Spherical)
reload(CaptureView)

#global variables
stop = 720

Rot1 = 0
Rot2 = 0
Rot3 = 0

#Hor Angles
HorAngle1 = 20
HorAngle2 = 20
HorAngle3 = 20

#Ver angles
VerAngle1 = 0.1
VerAngle2 = 0.1
VerAngle3 = 0.1

#Radius 
Rad1 = 100
Rad2 = 100 / 5 
Rad3 = 100 / 5

#PolyLine Control
polyX = 3
polyY = 3
height = 3

Points =[]

#loop running TrigCir 
while Rot1 <= stop:
    Rot1+= 5
    Rot2+= 5
    Rot3+= 5
    
    #pause between every point
    #rs.Sleep(10)
    
    #numbers used to create objects
    pt1 = TrigCirc(HorAngle1,VerAngle1,Rad1,Rot1,0,0,0,"ThreeD")
    pt2 = TrigCirc(HorAngle2,VerAngle2,Rad2,Rot2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(HorAngle3,VerAngle3,Rad3,Rot3,pt2[0],pt2[1],pt2[2],"ThreeD")
    
    #creates objects
    pts = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    Points.append(pts)
    
    
    
    

#lines between points
Lines = rs.AddPolyline(Points)
rs.ObjectPrintWidth(Lines,.2)
rs.ObjectColor(Lines,(1,0,0))

#polylines


Vert = rs.AddPoint((pt3[0],pt3[1],pt3[2]+2))

Path = rs.AddLine(pts,Vert)

Surf = rs.ExtrudeCurve(Lines,Path)

SurfSet = rs.ExplodePolysurfaces(Surf)

#center 
Origin = rs.AddPoint(0,0,pt3[2])

#create a list of paths for extrusions
Paths = []
for i in range(len(Points)):
    Path = rs.AddLine(Points[i],Origin)
    Paths.append(Path)

#extrudes surface 
for i in range(len(SurfSet)):
    rs.ExtrudeSurface(SurfSet[i],Paths[i])

#render mode
#for view in views:
#    rs.ViewDisplayMode(view,'Rendered')

#color 
#rs.ObjectPrintWidth(Rail,.2)
#rs.ObjectColor(Rail,(255,100,100))

rs.ZoomExtents()

rs.CreatePreviewImage("Harris While Loop 1.jpg")
#GetCaptureView(2,"Harris While Loop 1")