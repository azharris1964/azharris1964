// pong exercise

//variables for ball
var ballX = 50;
var ballY = 50;
var diameter = 50;
var directionX = 6;
var directionY = 5;

//variables for paddle
var rectX;
var rectY;
var rectW = 150;
var rectH = 25;

var started = false;
var score = 0;


function setup() {
    createCanvas(800,800);
    
}

function draw(){
    background(0);
    
    //ball bounces off wall
    ballX = ballX + directionX; // ballX += directionX
     ballY = ballY + directionY;
    
    if (ballX < 0 || ballX > width){
        directionX = -directionX;
    }
    
    if (ballY < 0 || ballY > height){
        directionY = -directionY; 
    }
    
    //detect collision with paddle
    
    if((ballX > rectX && ballX < rectX + rectW) && (ballY + (diameter/2) >= rectY)){
        directionX*= -1;
        directionY*= -1;
        score++;        
    }
    
    //draw ball
    fill(255);
    ellipse(ballX, ballY, diameter, diameter);
    
    //draw paddle
    fill(255);
    rectX = map(mouseX, 0, width, 0, 800, true);
    rect(rectX, rectY, rectW, rectH);
    
    //update paddle location
    if (!started){
        rectX = width/2;
        rectY = height - 100;
        started = true;
    }
    
    
    //fail and reset
    if(ballY >= height){
        ballX = width/2;
        ballY = height/4;
        score--;
    }
    
    //draw score
    fill(255);
    textSize(24);
    text ("Score: " + score, 10, 25);
    
    //set win condition
    if(score >= 5){
        textSize(50);
        fill(255);
        text("You Win", 330, 400)
    }
    
    if(score <= -5){
       textSize(50);
        fill(255);
        text("You Lose", 330, 400) 
        
    }
    
    
}

    

function keyPressed(){
    
    if(keyCode === LEFT_ARROW){
        
        rectX = rectX -50;
    }
    
     if(keyCode === RIGHT_ARROW){
        
        rectX = rectX +50;
    }
}