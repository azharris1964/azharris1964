/////////////////////////////////
//          CSMA101            //
//          Fall '19           //
//      Professor Theohar      //
//      Armontae Harris        //
//      (346) 269 - 5301       //
//        Ball Homework        //
/////////////////////////////////

var startX;
var startY;
var directionX;
var directionY;

var color;
var edge;
function setup() {
    createCanvas(500,500);  
    background(255);
    //starting point
    startX = width/2;
    startY = height/2;
    
    //movement
    directionX = 4;
    directionY = 6;
    
}

function draw () {
        

    //starting point + movement
    startX = startX + directionX;
    startY = startY + directionY;
    
    if( startX > (width)) {
        
        directionX = -directionX
    }
    
    if( startX < (0)) {
        
        directionX = -directionX
    }
    if( startY < (0)) {
        
        directionY = -directionY
    }
    if( startY > (height)) {
        
        directionY = -directionY
    }
   
    edge = map(startX, 0, width, 0, 5, true);
    color = map(startX, 0, width, 0, 255);
    fill(color);
    stroke (edge);
    rect(startX, startY,random(50, 100), random(50, 100));
    
    
}