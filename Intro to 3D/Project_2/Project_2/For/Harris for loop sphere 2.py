#Armontae_Harris_2.22.21
#Draws an object with spherical motion


#imports classes
import Spherical
from Spherical import TrigCirc

#reloads files
from imp import reload
reload(Spherical)

import LinearColorGradient
from LinearColorGradient import LinearColor
reload(LinearColorGradient)

#imports libraries
import rhinoscriptsyntax as rs
import math
import random

#setup
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

#global variables
Radius = 20
step = .1

#list
pts = []
ptsI = []

#range of loop
stop = 100

#hor angle
HorAngle1 = 10
HorAngle2 = 20
HorAngle3 = 40

#ver angle
VerAngle1 = 0.01
VerAngle2 = 0.01
VerAngle3 = 0.01

#radius 
rad1 = 100
rad2 = 200 
rad3 = 100 

#Rotation
rot1 = 2
rot2 = 2
rot3 = 3

#polyLine Control
polyX = 3
polyY = 3
polyZ = 3

#TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)
for i in range(1,stop,1):
    
    rot1  = 2*i
    rot2  = 5*i
    rot3  = 10*1
    p = random.randint(10,40)
    pt1 = TrigCirc(HorAngle1,VerAngle1,rad1,rot1,0,0,0,"ThreeD")
    pt2 = TrigCirc(HorAngle2,VerAngle2,rad2,rot2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(HorAngle3,VerAngle3,rad3,rot3,pt2[0],pt2[1],pt2[2],"ThreeD")
    ptI = rs.AddPoint(pt2[0],pt2[1],pt2[2])
    pt = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    pts.append(pt)
    
    ptsI.append(ptI)

#adds polylines
Rail = rs.AddPolyline(pts)
Vert = rs.AddPoint((pt3[0],pt3[1],pt3[2]+2))
Path = rs.AddLine(pt,Vert)
Surf = rs.ExtrudeCurve(Rail,Path)

SurfSet = rs.ExplodePolysurfaces(Surf)

#create center 
Origin = rs.AddPoint(pt2[0],pt2[1],pt2[2])

#create a list of paths for extrusions
Paths = []
for i in range(len(pts)):
    Path2 = rs.AddLine(pts[i],ptsI[i])
    Paths.append(Path2)

Cv = []
colors = []
C = 0

#color interval per solid
ColorInterval = 255/(len(SurfSet))

#build a list of color scalars 
for i in range(len(SurfSet)):
    C += ColorInterval/255
    Cv.append(C)
    color = LinearColor(255,255,255,12,59,101,Cv[i])
    colors.append((color[0],color[1],color[2]))

Origin = rs.AddPoint(0,0,pt3[2])

#extrudes
for i in range(len(SurfSet)):
    rs.ExtrudeSurface(SurfSet[i],Paths[i])

#show a zoomed in view right when program runs
rs.ZoomExtents()

rs.CreatePreviewImage("Harris_forLoop ex1.jpg")