/////////////////////////////////
//          CSMA101            //
//          Fall '19           //
//      Professor Theohar      //
//      Armontae Harris        //
//      (346) 269 - 5301       //
//      Curtain Exercise  2    //
/////////////////////////////////




//curtain exercise

var img1;
var img2;
var img3;
var totalCircles;
var x, y;
var desiredColor;
var c;
var d;

function preload(){
    img1 = loadImage ("data/tist.jpg");
    img2 = loadImage ("data/tust.jpg");
    img3 = loadImage ("data/trust.jpg");
    
}

function setup() {
    
    createCanvas(1200, 1200);
    background (255);
    
    //loading image data
    img1.loadPixels();
    img2.loadPixels();
    img3.loadPixels();
    
    //initialize values
    totalCircles = 300;
    y = 0;
    c = 1;
    d = 1;
        
}

function draw() {
    
    //set circle size based off totalCircles
    var circleSize = width/totalCircles;
    
    //draw circles
    var currentCircle = 0;
    
    //this keeps the size proportional to your width
    while(currentCircle < totalCircles){
        x = currentCircle * circleSize;
        
    
    
    //Get color 
    var desiredColor1 = getColor1();
    var desiredColor2 = getColor2();
    var desiredColor3 = getColor3();
        
if(keyCode === UP_ARROW){
       
        d = -d;
    }
if(keyCode === DOWN_ARROW){
       
        d = d;
    }
    
    if(c>0){
        
        fill(desiredColor1);
    }
    
    if(c<0){
        
        fill(desiredColor2);
    }
        if(d<0){
        
        fill(desiredColor3);
    }
    triangle(x, y, x + 10, y + 10, x, y + 10);
    currentCircle++;
        
    }
    
    //move down a row
    y = y + circleSize;
//    y = y + circleSize;
//    y = y + circleSize;
    //start over at top
    if(y > 1200){
        totalcircles = random(50, 100);
        c =-c;
        y = 0;
//        d = -d;
        
    }
    
    
    
    
}

///////////////
function getColor1() {
    var desiredColor1 = img1.get(floor(x), floor(y));
    
    return desiredColor1;
    
}

function getColor2() {
    var desiredColor2 = img2.get(floor(x), floor(y));
    return desiredColor2;
    
}

function getColor3() {
    var desiredColor3 = img3.get(floor(x), floor(y));
    return desiredColor3;
    
}