import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🏀 NBA Arcade Ultimate", layout="wide")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

body{
    margin:0;
    overflow:hidden;
    font-family:Arial;
    background:linear-gradient(135deg,#000,#ff6600);
}

/* SCOREBOARD */
#ui{
    color:white;
    text-align:center;
    font-size:24px;
    padding:10px;
    font-weight:bold;
}

/* COURT */
#court{
    position:relative;
    width:100%;
    height:600px;
    background:linear-gradient(to top,#8B5A2B,#DEB887);
    border-top:5px solid white;
}

/* PLAYER */
#player{
    position:absolute;
    bottom:40px;
    left:50%;
    font-size:65px;
    transition:0.08s;
}

/* HOOP */
#hoop{
    position:absolute;
    top:80px;
    left:20%;
    font-size:75px;
    animation:moveHoop 2.8s infinite alternate;
}

/* DEFENDER */
#defender{
    position:absolute;
    bottom:40px;
    left:30%;
    font-size:65px;
    animation:defenderMove 2s infinite alternate;
}

/* BALL */
#ball{
    position:absolute;
    font-size:35px;
    display:none;
}

/* POWER SHOT EFFECT */
.fire{
    filter: drop-shadow(0 0 10px orange);
    transform: scale(1.2);
}

@keyframes moveHoop{
    from{left:10%;}
    to{left:80%;}
}

@keyframes defenderMove{
    from{left:20%;}
    to{left:70%;}
}

</style>
</head>

<body>

<div id="ui">
🏀 Score: <span id="score">0</span> |
🪙 Coins: <span id="coins">0</span> |
⏱️ Time: <span id="time">60</span>
</div>

<div id="court">

<div id="hoop">🗑️</div>
<div id="player">⛹️</div>
<div id="defender">🧍</div>
<div id="ball">🏀</div>

</div>

<script>

let score=0;
let coins=0;
let time=60;

let streak=0;
let fireMode=false;

let playerX=50;

const player=document.getElementById("player");
const hoop=document.getElementById("hoop");
const ball=document.getElementById("ball");
const defender=document.getElementById("defender");

document.addEventListener("keydown",function(e){

// MOVE LEFT
if(e.key==="ArrowLeft"){
playerX-=3;
if(playerX<0) playerX=0;
player.style.left=playerX+"%";
}

// MOVE RIGHT
if(e.key==="ArrowRight"){
playerX+=3;
if(playerX>95) playerX=95;
player.style.left=playerX+"%";
}

// SHOOT
if(e.code==="Space"){

ball.style.display="block";
ball.style.left=player.style.left;

let height=80;

let shoot=setInterval(()=>{

height+=14;
ball.style.bottom=height+"px";

// FINISH SHOT
if(height>430){
clearInterval(shoot);

let hoopX=hoop.offsetLeft;
let playerPos=player.offsetLeft;

// HIT DETECTION
if(Math.abs(hoopX-playerPos)<120){

streak++;
score+=2;
coins+=5;

// FIRE MODE
if(streak>=3){
fireMode=true;
score+=3;
document.getElementById("ball").classList.add("fire");
}

if(streak>=5){
score+=5;
coins+=10;
}

document.getElementById("score").innerHTML=score;
document.getElementById("coins").innerHTML=coins;

}

else{
streak=0;
fireMode=false;
document.getElementById("ball").classList.remove("fire");
}

ball.style.display="none";
height=80;

}

},15);

}

});

// TIMER
setInterval(()=>{
time--;
document.getElementById("time").innerHTML=time;

if(time<=0){
alert("GAME OVER! Final Score: " + score);
location.reload();
}

},1000);

</script>

</body>
</html>
""", height=750)
