def setup():
    size(800, 800)  
    print("Hello from setup")

def draw():
    fill(map(mouseX, 0, 1000, 0, 0), 0, map(mouseY, 0, 1000, random(0, 255), 5))  
   # noStroke()
    if mousePressed:                     # if the mouse is pressed
        rect(mouseX, mouseY, random(0, 150), random(0, 150))  # draw a rectangle
