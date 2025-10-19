import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors Game", page_icon="🎮")
st.title("🪨 Rock ✋ Paper ✌️ Scissors")
st.markdown("### Play against the computer — test your luck and reflexes!")

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# Logic 
choices = {"rock": -1, "paper": 0, "scissor": 1}
reverse_choices = {v: k for k, v in choices.items()}

# User selection 
user_choice = st.selectbox("Choose your move:", list(choices.keys()))
play_button = st.button("🎮 Play")

if play_button:
    user = choices[user_choice]
    computer = random.choice(list(choices.values()))

    st.write(f"**You chose:** {reverse_choices[user].capitalize()}")
    st.write(f"**Computer chose:** {reverse_choices[computer].capitalize()}")

    if computer == user:
        st.info("🤝 It's a draw!")
    elif (computer - user) in (-1, 2):
        st.success("🎉 You win!")
        st.session_state.user_score += 1
    else:
        st.error("💻 Computer wins!")
        st.session_state.computer_score += 1

#  Scoreboard 
st.markdown("---")
st.subheader("🏆 Scoreboard")
st.write(f"👤 You: {st.session_state.user_score}")
st.write(f"💻 Computer: {st.session_state.computer_score}")

if st.button("🔄 Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.experimental_rerun()

st.markdown("---")
st.caption("Made by Anas in Streamlit")