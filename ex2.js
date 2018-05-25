/*
space invaders
*/

window.onload = function(){
  canvas = document.createElement("canvas");
  canvas.width = 640;
  canvas.height = 480;
  //adding the canvas to the HTML
  document.body.appendChild(canvas);
  pen = canvas.getContext("2d");
  // scan for keyboard inputs
  //document.addEventListener('keydown',keyPush);
  var fps = 30;
  setInterval(update,1000/fps);
  //enemy spawn rate
  setInterval(spawn,1000);

  //mouse lisener
  document.addEventListener("mousemove", mouseMoveHandler, false);
  document.addEventListener("mousedown", mouseClickHandler, false);

  ship = new Image();
  ship.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS69C1AMBPxPGU6yuGVkVx65DUjP2rJiUezVnZt2utLdf9NxJGQUQ";

};

player_x = player_y = 100;
player_speed = 15;
player_dim = 40;

lives = 3;
score = 0;

enemy_list = [];
enemy_speed = 5;
enemy_dim = 25;

shots_list = [];
shot_speed = 7;
shot_dim = 4;

function update(){
  pen.fillStyle = 'black';
  pen.fillRect(0,0,canvas.width,canvas.height);
  
  pen.drawImage(ship,player_x - player_dim / 2,player_y - player_dim / 2,player_dim,player_dim);
  
  //pen.fillRect(player_x - player_dim/2,player_y - player_dim/2, player_dim,player_dim);
  
  pen.fillStyle = 'white';
  pen.font ='20px Arial';
  pen.fillText("Lives: "+ lives,canvas.width/20,canvas.height/20);
  pen.fillText("Score: "+ score,canvas.width/20,canvas.height/10);
  
  pen.fillStyle = 'lime';
  for(var s = 0; s < shots_list.length; s++){
    shots_list[s].x += shot_speed;
    
    pen.fillRect(shots_list[s].x - shot_dim/2, shots_list[s].y - shot_dim/2, shot_dim,shot_dim);
  
    for(var e = enemy_list.length - 1; e >= 0; e--){
      var diff_x = Math.abs(enemy_list[e].x - shots_list[s].x);
      var diff_y = Math.abs(enemy_list[e].y-shots_list[s].y);
      var dist = Math.sqrt(diff_x  *diff_x + diff_y * diff_y);
    
    //detects if a shot hits the enemy
    if(dist<(shot_dim + enemy_dim)/2){
      enemy_list.splice(e,1);
      score++;
    }
  }
  }
  
  
  pen.fillStyle = 'red';
  for (var e = 0; e < enemy_list.length; e++){
    enemy_list[e].x -= enemy_speed;
    
    pen.fillRect(enemy_list[e].x - enemy_dim/2,enemy_list[e].y - enemy_dim/2,enemy_dim,enemy_dim);
    
    var diff_x_enem = Math.abs(enemy_list[e].x - player_x);
    var diff_y_enem = Math.abs(enemy_list[e].y - player_y);
    var dist_enem = Math.sqrt(diff_x_enem * diff_x_enem + diff_y_enem * diff_y_enem);

    //detects if enemy hit our guy
    if(dist_enem < (player_dim + enemy_dim)/2){
      //clear the stats and reset the player if he gets hit
      shots_list = [];
      enemy_list = [];
      player_x = player_y = 100;
      lives--;
      break;
        }
  
  }


  if(lives <= 0){
    //draw black background
    pen.fillStyle = "black";
    pen.fillRect(0,0,canvas.width,canvas.height);
    //game over
    pen.font = "40px Impact";
    pen.fillStyle = 'red';
    pen.fillText("Game Over",canvas.width*.35,canvas.height/2);
    pen.fillText("Score: "+ score,canvas.width*.40,canvas.height*.7);
  }
}
  
function spawn(){
  enemy_list.push({x: canvas.width, y: Math.random()*canvas.height});
}


function mouseMoveHandler(e) {
 player_y = e.clientY
}

function mouseClickHandler(e) {
 // this checks for the left button
 if(e.button == 0){
   shots_list.push({ x: player_x, y: player_y });
 }
}


/*
function keyPush(evt){
  switch(evt.keyCode){
     case 32:// space bar
     shots_list.push({x: player_x, y: player_y});
      break;
     case 37:// left
     player_x -= player_speed;
      break;
     case 38:// up
     player_y -= player_speed;
      break;
     case 39:// right
     player_x += player_speed;
      break;
     case 40:// down
     player_y += player_speed;
      break;
  }*/

