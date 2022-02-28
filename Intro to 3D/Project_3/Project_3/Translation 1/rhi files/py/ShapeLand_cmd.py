#Armontae Harris
#Spherical motion command

#import libraries
import rhinoscriptsyntax as rs

import math
import random
import Rhino

from math import radians
from math import cos
from math import sin

 
import System
import scriptcontext as sc

#custom modules
def TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient):
    

    #loop to create points on sphere
    for i in range(Rotation):
        
        Hor = radians(HorAngle*i)
        Ver = radians(VerAngle*i)
        
        if Orient == "ThreeD":
        
    
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = cos(Ver)*Radius + CenterZ
            
        if Orient == "Top":
            
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = 0 + CenterZ
            
        if Orient == "Front":
        
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = cos(Ver)*Radius + CenterZ
            z = 0 + CenterY
            
        if Orient == "Oblique":
        
    
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) - cos(Ver)*Radius*.9 + CenterZ + CenterY
            z = 0 + CenterZ           



    return(x,y,z)

def GetCaptureView(Scale,FileName,NewFolder):

    view = sc.doc.Views.ActiveView;
    if view:
        view_capture = Rhino.Display.ViewCapture()
        view_capture.Width = view.ActiveViewport.Size.Width*Scale
        view_capture.Height = view.ActiveViewport.Size.Height*Scale
        view_capture.ScaleScreenItems = False
        view_capture.DrawAxes = False
        view_capture.DrawGrid = False
        view_capture.DrawGridAxes = False
        view_capture.TransparentBackground = False
        bitmap = view_capture.CaptureToBitmap(view)
        if bitmap:
            #locate the desktop and get path
            folder = System.Environment.SpecialFolder.Desktop
            path = System.Environment.GetFolderPath(folder)
            #convert foldername and file name sto string
            FName = str(NewFolder)
            File = str(FileName)
            #combine foldername and desktop path
            Dir = System.IO.Path.Combine(path,FName)
            #creat path to tje new folder
            NFolder = System.IO.Directory.CreateDirectory(Dir)
            Dir = System.IO.Path.Combine(Dir,FileName +".png")
            print (Dir)
            #save the file
            bitmap.Save(Dir, System.Drawing.Imaging.ImageFormat.Png);

def LinearColor(R,G,B,R2,G2,B2,ColorPercentage):
    #creates colored gradient based on point system using (R,G,B)
    Rdiff = R2 - R
    Gdiff = G2 - G
    Bdiff = B2 - B
    t = ColorPercentage
    R3 = float(R + Rdiff*t)
    G3 = float(G + Gdiff*t)
    B3 = float(B + Bdiff*t)
    
    color = rs.CreateColor(R3,G3,B3)
    return (color)

def WriteTxt(Strings,FileName,FolderName):
    FName = str(FolderName)
    File = str(FileName)
    #combine foldername and desktop path
    folder = System.Environment.SpecialFolder.Desktop
    path = System.Environment.GetFolderPath(folder)
    Dir = System.IO.Path.Combine(path,FName)
    NFolder = System.IO.Directory.CreateDirectory(Dir)
    Dir = System.IO.Path.Combine(Dir,File +".txt")
    myText = open(Dir,"w") 

   
    myString = '\n'.join(Strings)
    myText.write(myString)
    myText.close()

def SaveObj(Objects,FileName,NewFolder):
    rs.SelectObjects(Objects)
    
    folder = System.Environment.SpecialFolder.Desktop
    path = System.Environment.GetFolderPath(folder)
    #convert foldername and file name sto string
    FName = str(NewFolder)
    File = str(FileName)
    #combine foldername and desktop path
    Dir = System.IO.Path.Combine(path,FName)
    NFolder = System.IO.Directory.CreateDirectory(Dir)
    Dir = System.IO.Path.Combine(Dir,FileName +".obj")
    cmd = "_-Export " + Dir + " _Enter PolygonDensity=1 _Enter"
    rs.Command(cmd)

CaptureView = False


__commandname__ = "ShapeLand"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    #setup
    
    Solid = True
    DeleteObjects = rs.GetString("Would you like to clean your canvas? y/n")
    
    if DeleteObjects == "y":
        
        delSet = rs.AllObjects(True)
        rs.DeleteObjects(delSet)
        
        rs.UnitSystem(8)
        
        #list
        pts = []
        ptsI = []
        
        #global variables
        
        stop = int(rs.GetReal("How many points would you like?", minimum=5, maximum=1000))
        
        RValue1 = int(rs.GetReal("How many first rotations?", minimum=2, maximum=1000))
        RValue2 = int(rs.GetReal("How many second rotations?", minimum=2, maximum=1000))
        RValue3 = int(rs.GetReal("How many third rotations?", minimum=2, maximum=1000))
        
        Sides = int(rs.GetReal("How many sides would you like?", minimum=3, maximum=1000))
        HorAngle = 360/Sides
        VerAngle = 0.01
        
        rad = int(rs.GetReal("What radius would you like to use?", minimum=10, maximum=1000))
        
        Red = rs.GetReal("On a scale of 0 to 255, how excited are you today?", minimum=0, maximum=255)
        Green = rs.GetReal("On a scale of 0 to 255, how calm do you feel today?", minimum=0, maximum=255)
        Blue = rs.GetReal("On a scale of 0 to 255, how much fun are you having?", minimum=0, maximum=255)
        
        step = int(rs.GetReal("How thick should your creation be?", minimum=0, maximum=50))
        
        
        
        #TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)
        for i in range(1,stop,1):
            
            rot1 = RValue1*i
            rot2 = RValue2*i
            rot3 = RValue3*i
            
            pt1 = TrigCirc(-HorAngle,VerAngle,rad,rot1,0,0,0,"ThreeD")
            pt2 = TrigCirc(HorAngle,VerAngle,rad/3,rot2,pt1[0],pt1[1],pt1[2],"ThreeD")
            pt3 = TrigCirc(HorAngle/3,VerAngle,rad/3,rot3,pt2[0],pt2[1],pt2[2],"ThreeD")
            
            ptI = rs.AddPoint(pt2[0],pt2[1],pt2[2])
            
            pt = rs.AddPoint(pt3[0],pt3[1],pt3[2])
            
            pts.append(pt)
            
            ptsI.append(ptI)
        
        #adds polylines
        Rail = rs.AddPolyline(pts)
        
        if Solid == True:
            Vert = rs.AddPoint((pt3[0],pt3[1],pt3[2]+2))
            Path = rs.AddLine(pt,Vert)
            #rs.ExtrudeCurve(Rail,Path)
            Surf = rs.ExtrudeCurve(Rail,Path)
        
        SurfSet = rs.ExplodePolysurfaces(Surf)
        
        #create center 
        Origin = rs.AddPoint(pt2[0],pt2[1],pt2[2])
        
        #create a list of paths for extrusions
        Paths = []
        for i in range(len(pts)):
            Path2 = rs.AddLine(pts[i],ptsI[i])
            Paths.append(Path2)
        
        #build a list of color scalars 
        Cv = []
        colors = []
        C = 0
        
        #color interval per solid
        ColorInterval = 255/(len(SurfSet))
        
        #build a list of color scalars 
        for i in range(len(SurfSet)):
            C += ColorInterval/255
            Cv.append(C)
            color = LinearColor(200,220,255,Red,Green,Blue,Cv[i])
            colors.append(color)
        
        
        
        #extrudes
        Solids = []
        for i in range(len(SurfSet)):
            Solid = rs.ExtrudeSurface(SurfSet[i],Paths[i])
            Mat = rs.AddMaterialToObject(Solid)
            rs.MaterialColor(Mat,colors[i])
            Solids.append(Solid)
        
        #clean up view
        PointsAll = rs.ObjectsByType(1,True,0)
        CurvesAll = rs.ObjectsByType(4,True,0)
        
        rs.HideObjects(PointsAll)
        rs.HideObjects(CurvesAll)
        rs.HideObjects(Surf)
        rs.HideObjects(SurfSet)
        
        #view
        views = rs.ViewNames()
        for view in views:
            rs.ViewDisplayMode(view,'Rendered')
        rs.ZoomExtents()
        
        #Generate image
        
        CaptureView = rs.GetString("Would you like a photo souvenir of your creation? y/n")
        
        if CaptureView == "y":
            FileName  = rs.GetString("What is the title of your creation?")
            NewFolder = FileName
            Ready = rs.GetString("Please set your viewport to an 800 x 800 pixel size. Ready? y/n")
            
            if Ready == "y":
                rs.ZoomExtents()
                rs.Command("-GroundPlane ShowPanel No Options On=No Enter Enter")
    
                GetCaptureView(2,FileName + str(RValue1) +"_"+ str(RValue2) +"_"+ str(RValue3)+str(color),NewFolder)
                
                #WriteTxt(Strings,Filename,Foldername)
                WriteTxt(["File_Name_" + str(FileName),"Stop_" + str(stop), "Rotations1_" + str(RValue1),"Rotations2_" + str(RValue2),
                "Rotations3_" + str(RValue3), "Sides_" + str(Sides), "Radius_" + str(rad),
                "Red_" + str(Red),"Green_" + str(Green), "Blue_" + str(Blue),"Height_" + str(step)],FileName,NewFolder)
            else: 
                pass
        else:
            pass
        SaveObject = rs.GetString("Would you like a 3-D souvenir of your creation? y/n")
        
        if SaveObject == "y":
            SaveObj(Solids,FileName,NewFolder)
        
        
        
        print ("Done. You can find your file at  " + str(NewFolder))
    else:
        print("You must restart to proceed. Please clear your canvas to continue.")

RunCommand(True)
