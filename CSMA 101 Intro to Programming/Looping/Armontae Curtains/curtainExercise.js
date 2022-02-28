/////////////////////////////////
//          CSMA101            //
//          Fall '19           //
//      Professor Theohar      //
//      Armontae Harris        //
//      (346) 269 - 5301       //
//      Curtain Exercise  1    //
/////////////////////////////////

var img1;
var img2;
var totalCircles;
var x, y;
var desiredColor;
var c;

function preload(){
    img1 = loadImage("data/test.jpg")
    img2 = loadImage("data/teest.jpg")
    
    
}

function setup (){
    
    createCanvas (800, 1000);

    
    
    img1.loadPixels();
    img2.loadPixels();
    
    
    totalCircles = 100;
    y = 0;
    c = 1;
    
}

function draw(){
    //set circle size based off totalCircles
    var circleSize = width/totalCircles;
    
    
    //draw circles
    var currentCircle = 0;
    
    
    //this keeps the size proportional to your width
    while(currentCircle < totalCircles){
        x = currentCircle * circleSize;
        
    //get color
    var desiredColor1 = getColor1();
    var desiredColor2 = getColor2();
    
    if(c > 0){
        
        fill(desiredColor1);
        translate(height/2);
        rotate(radians(1/2));
    }
    
    if(c < 0){
        
        fill(desiredColor2);
        translate(height/2);
        rotate(radians(1/2));
    }
    
    rect(x, y, circleSize, circleSize);
//    ellipse(x, y, circleSize, circleSize);
    currentCircle++;
}
    //move down a row
    y = y + circleSize
    
    //start over at top
    if(y > height){
        totalCircles = random (80, 100);
        c = -c;
        y = 0;
    }
}

//////////////////////
function getColor1() {
    var desiredColor1 = img1.get(floor(x), floor(y));
    return desiredColor1;
}

function getColor2() {
    var desiredColor2 = img2.get(floor(x), floor(y));
    return desiredColor2;
    
}





