import streamlit as st
import random

st.title("🎮 Guess My Number Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1,20)
    st.session_state.attempts = 0

st.write("I'm thinking of a number between **1 and 100**.")

guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("📉 Too Low! Try again.")
    elif guess > st.session_state.number:
        st.warning("📈 Too High! Try again.")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")

st.write(f"Attempts: {st.session_state.attempts}")

# Restart button
if st.button("Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.experimental_rerun()