st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#ff9a3c,#ffd166);
}

/* Game Title */
.title {
    text-align:center;
    font-size:70px;
    font-weight:bold;
    color:white;
    text-shadow:4px 4px 10px black;
    animation: glow 2s infinite;
}

/* Cards */
.game-card {
    background:white;
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,0.3);
    margin:10px;
}

/* Gold Counter */
.gold {
    color:gold;
    font-size:30px;
    font-weight:bold;
}

/* XP Counter */
.xp {
    color:deepskyblue;
    font-size:30px;
    font-weight:bold;
}

/* Question Box */
.question-box {
    background:#fff8dc;
    border-left:10px solid orange;
    padding:20px;
    border-radius:15px;
    font-size:24px;
}

/* Board Spaces */
.space {
    width:90px;
    height:90px;
    border-radius:15px;
    border:3px solid orange;
    display:inline-flex;
    justify-content:center;
    align-items:center;
    font-size:40px;
    margin:4px;
    background:white;
    transition:0.3s;
}

.space:hover {
    transform:scale(1.1);
}

.player {
    background:lime;
    animation:bounce 1s infinite;
}

/* Achievement */
.achievement {
    background:gold;
    padding:15px;
    border-radius:15px;
    font-size:25px;
    font-weight:bold;
    text-align:center;
}

/* Win Screen */
.win {
    background:gold;
    color:black;
    font-size:50px;
    font-weight:bold;
    text-align:center;
    border-radius:20px;
    padding:25px;
}

/* Animations */
@keyframes glow {
    0% {text-shadow:0 0 10px white;}
    50% {text-shadow:0 0 30px yellow;}
    100% {text-shadow:0 0 10px white;}
}

@keyframes bounce {
    0% {transform:translateY(0);}
    50% {transform:translateY(-10px);}
    100% {transform:translateY(0);}
}

</style>
""", unsafe_allow_html=True)
