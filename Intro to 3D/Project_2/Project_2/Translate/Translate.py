
#Armontae Harris
#2.25.2021
import rhinoscriptsyntax as rs
import random

#refresh 
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

#creates a list 
points =[]
spheres =[]
for i in range(0,100,20):
    for j in range(0,100,20):
        p = random.randint(0,20)
        pt= rs.AddPoint(i,j,p)
        Sphere = rs.AddSphere(pt,p)
        spheres.append(Sphere)
        points.append(pt)


Mass = rs.BooleanUnion(spheres)


for i in Mass:
    Mat = rs.AddMaterialToObject(i)
    rs.MaterialColor(Mat,(0,200,255))

#zoom to the object and create a jpgs
rs.ZoomExtents()
rs.CreatePreviewImage("Harris.jpg")

