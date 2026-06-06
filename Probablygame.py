import streamlit as st
import random

st.set_page_config(
    page_title="🏀 Basket Français",
    page_icon="🏀",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0055A4,#FFFFFF,#EF4135);
}

.title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#0055A4;
    text-shadow:2px 2px 8px white;
}

.subtitle{
    text-align:center;
    font-size:22px;
    color:#222;
}

.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.2);
    text-align:center;
}

.score{
    background:linear-gradient(135deg,#0055A4,#EF4135);
    color:white;
    padding:20px;
    border-radius:20px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("""
<div class="title">🏀 Basket Français 🏀</div>
<div class="subtitle">Essayez de marquer le plus de paniers possible !</div>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "score" not in st.session_state:
    st.session_state.score = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# ---------- Scoreboard ----------
st.markdown(
f"""
<div class="score">
🏆 Score: {st.session_state.score}<br>
🎯 Tentatives: {st.session_state.attempts}
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------- Difficulty ----------
difficulty = st.selectbox(
    "Choisissez la difficulté",
    ["Facile", "Moyen", "Difficile"]
)

if difficulty == "Facile":
    chance = 80
elif difficulty == "Moyen":
    chance = 60
else:
    chance = 40

# ---------- Court ----------
st.markdown("""
<div class="card">
<h2>🏀 Terrain de Basket</h2>
<p>Cliquez sur le bouton pour tirer !</p>
</div>
""", unsafe_allow_html=True)

# ---------- Shoot ----------
if st.button("🏀 Tirer le ballon !"):

    st.session_state.attempts += 1

    shot = random.randint(1,100)

    if shot <= chance:
        st.session_state.score += 2
        st.success("🎉 PANIER ! +2 points")
        st.balloons()
    else:
        st.error("❌ Raté !")

# ---------- Stats ----------
if st.session_state.attempts > 0:

    percentage = (
        st.session_state.score /
        (st.session_state.attempts * 2)
    ) * 100

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🏆 Score", st.session_state.score)

    with col2:
        st.metric("📈 Réussite", f"{percentage:.1f}%")

# ---------- Reset ----------
if st.button("🔄 Nouvelle Partie"):
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.rerun()

st.markdown("---")
st.markdown(
"<center><h3>🇫🇷 Vive le Basket Français ! 🏀</h3></center>",
unsafe_allow_html=True
)
