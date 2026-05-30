import streamlit as st
import random

st.title("🎲 Mathopoly")

if "position" not in st.session_state:
    st.session_state.position = 0
    st.session_state.coins = 20
    st.session_state.message = ""

board = [
    "START",
    "MEAN",
    "MEDIAN",
    "MODE",
    "PROBABILITY",
    "BONUS",
    "CHANCE",
    "TAX",
    "FORWARD",
    "MEAN",
    "MEDIAN",
    "MODE",
    "PROBABILITY",
    "CHANCE",
    "BONUS",
    "FINISH"
]

questions = {
    "MEAN": [
        ("What is the mean of 2, 4, 6?", "4"),
        ("What is the mean of 5, 10, 15?", "10")
    ],
    "MEDIAN": [
        ("What is the median of 1, 3, 5?", "3"),
        ("What is the median of 2, 4, 6, 8, 10?", "6")
    ],
    "MODE": [
        ("What is the mode of 2, 2, 3, 4?", "2"),
        ("What is the mode of 5, 5, 5, 2, 3?", "5")
    ],
    "PROBABILITY": [
        ("Probability of heads on a coin flip?", "1/2"),
        ("A die has 6 sides. Probability of rolling a 3?", "1/6")
    ]
}

st.write(f"📍 Position: {st.session_state.position}")
st.write(f"🪙 Coins: {st.session_state.coins}")

if st.button("🎲 Roll Dice"):
    roll = random.randint(1, 6)
    st.session_state.position += roll

    if st.session_state.position >= len(board) - 1:
        st.session_state.position = len(board) - 1

    space = board[st.session_state.position]

    st.success(f"You rolled a {roll}!")
    st.write(f"You landed on **{space}**")

    if space in questions:
        q, a = random.choice(questions[space])
        st.session_state.question = q
        st.session_state.answer = a

    elif space == "BONUS":
        st.session_state.coins += 20
        st.session_state.message = "💰 Bonus! +20 coins"

    elif space == "TAX":
        st.session_state.coins -= 10
        st.session_state.message = "💸 Tax! -10 coins"

    elif space == "FORWARD":
        st.session_state.position += 2
        st.session_state.message = "🚀 Move forward 2 spaces!"

    elif space == "CHANCE":
        card = random.choice([
            ("Gain 15 coins!", 15),
            ("Lose 15 coins!", -15)
        ])
        st.session_state.coins += card[1]
        st.session_state.message = f"🎁 Chance Card: {card[0]}"

if st.session_state.message:
    st.info(st.session_state.message)

if "question" in st.session_state:
    st.subheader("🧠 Math Challenge")
    st.write(st.session_state.question)

    user_answer = st.text_input("Answer")

    if st.button("Submit"):
        if user_answer.strip() == st.session_state.answer:
            st.session_state.coins += 10
            st.success("✅ Correct! +10 coins")
        else:
            st.session_state.coins -= 5
            st.error(
                f"❌ Wrong! Answer: {st.session_state.answer}"
            )

        del st.session_state.question
        del st.session_state.answer

if st.session_state.position == len(board) - 1:
    st.balloons()
    st.header("🏆 You Win!")
    st.write(f"Final Coins: {st.session_state.coins}")
