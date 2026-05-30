import streamlit as st
import random

st.set_page_config(
    page_title="🏴‍☠️ Mathopoly Treasure Hunters",
    page_icon="🏴‍☠️",
    layout="wide"
)

# ---------------- STYLE ----------------

st.markdown("""
<style>

.main {
    background: linear-gradient(135deg, #ff9a3c, #ffd166);
}

.title {
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:white;
    text-shadow:3px 3px 8px black;
}

.card {
    background:white;
    padding:20px;
    border-radius:20px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
}

.board {
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
}

.space {
    width:90px;
    height:90px;
    margin:6px;
    border-radius:15px;
    border:3px solid #ff7b00;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:35px;
    background:white;
}

.player {
    background:#7CFC00;
    transform:scale(1.1);
}

.question {
    background:#fff8dc;
    border-left:10px solid orange;
    padding:20px;
    border-radius:15px;
    font-size:22px;
}

.win {
    background:gold;
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:45px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="title">🏴‍☠️ MATHOPOLY TREASURE HUNTERS 🏴‍☠️</div>',
    unsafe_allow_html=True
)

# ---------------- GAME STATE ----------------

if "position" not in st.session_state:
    st.session_state.position = 0
    st.session_state.gold = 50
    st.session_state.message = ""

# ---------------- BOARD ----------------

board = [
    "🏁", "➕", "📊", "🔢",
    "🎲", "💰", "🎁", "🦈",
    "🚀", "➕", "📊", "🔢",
    "🎲", "🌈", "💰", "🏆"
]

# ---------------- QUESTIONS ----------------

questions = {
    "➕": [
        ("What is the mean of 2, 4, 6?", "4"),
        ("What is the mean of 5, 10, 15?", "10"),
        ("What is the mean of 3, 6, 9?", "6")
    ],
    "📊": [
        ("What is the median of 1, 3, 5?", "3"),
        ("What is the median of 2, 4, 6, 8, 10?", "6"),
        ("What is the median of 5, 7, 9?", "7")
    ],
    "🔢": [
        ("What is the mode of 2,2,3,4?", "2"),
        ("What is the mode of 5,5,5,2,3?", "5"),
        ("What is the mode of 7,7,8,9?", "7")
    ],
    "🎲": [
        ("Probability of getting heads?", "1/2"),
        ("Probability of rolling a 3 on a die?", "1/6"),
        ("Probability of drawing a red card from 4 red and 4 blue cards?", "1/2")
    ]
}

# ---------------- STATS ----------------

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f'<div class="card">📍 Position<br>{st.session_state.position}</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f'<div class="card">💰 Gold<br>{st.session_state.gold}</div>',
        unsafe_allow_html=True
    )

# ---------------- BOARD DISPLAY ----------------

html = '<div class="board">'

for i, space in enumerate(board):

    if i == st.session_state.position:
        html += f'<div class="space player">{space}</div>'
    else:
        html += f'<div class="space">{space}</div>'

html += "</div>"

st.markdown(html, unsafe_allow_html=True)

# ---------------- LEGEND ----------------

st.info("""
➕ Mean | 📊 Median | 🔢 Mode | 🎲 Probability

💰 Treasure | 🎁 Chance Card | 🦈 Shark Attack

🚀 Speed Boost | 🌈 Rainbow Bridge | 🏆 Finish
""")

# ---------------- ROLL DICE ----------------

if st.button("🎲 Roll Dice"):

    roll = random.randint(1, 6)

    st.success(f"You rolled a {roll}!")

    st.session_state.position += roll

    if st.session_state.position >= len(board) - 1:
        st.session_state.position = len(board) - 1

    space = board[st.session_state.position]

    if space in questions:

        q, a = random.choice(questions[space])

        st.session_state.question = q
        st.session_state.answer = a

    elif space == "💰":

        st.session_state.gold += 25
        st.session_state.message = "💰 Treasure Chest! +25 Gold"

    elif space == "🦈":

        st.session_state.gold -= 15
        st.session_state.message = "🦈 Shark Attack! -15 Gold"

    elif space == "🚀":

        st.session_state.position = min(
            st.session_state.position + 3,
            len(board) - 1
        )

        st.session_state.message = "🚀 Speed Boost! Move 3 spaces!"

    elif space == "🌈":

        st.session_state.position = min(
            st.session_state.position + 2,
            len(board) - 1
        )

        st.session_state.message = "🌈 Rainbow Bridge! Jump ahead!"

    elif space == "🎁":

        card = random.choice([
            ("Find buried treasure! +30 Gold", 30),
            ("Pirate tax! -20 Gold", -20),
            ("Lucky map! +15 Gold", 15),
            ("Lost at sea! -10 Gold", -10)
        ])

        st.session_state.gold += card[1]
        st.session_state.message = card[0]

# ---------------- MESSAGE ----------------

if st.session_state.message:
    st.warning(st.session_state.message)

# ---------------- QUESTION ----------------

if "question" in st.session_state:

    st.markdown(
        f"""
        <div class="question">
        🧠 <b>Math Challenge</b><br><br>
        {st.session_state.question}
        </div>
        """,
        unsafe_allow_html=True
    )

    user_answer = st.text_input("Your Answer")

    if st.button("Submit Answer"):

        if user_answer.strip() == st.session_state.answer:

            st.session_state.gold += 10

            st.success("✅ Correct! +10 Gold")

        else:

            st.session_state.gold -= 5

            st.error(
                f"❌ Wrong! The answer was {st.session_state.answer}"
            )

        del st.session_state.question
        del st.session_state.answer

# ---------------- WIN ----------------

if st.session_state.position == len(board) - 1:

    st.balloons()

    st.markdown("""
    <div class="win">
    🏆 TREASURE FOUND! 🏆
    </div>
    """, unsafe_allow_html=True)

    st.write(f"## Final Gold: {st.session_state.gold}")

    if st.session_state.gold >= 100:
        st.success("👑 Pirate King Achievement Unlocked!")
