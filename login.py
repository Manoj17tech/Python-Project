import streamlit as st

# Demo user credentials
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "password123"
}

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Login function
def login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
    else:
        st.error("Invalid username or password")


# Logout function
def logout():
    st.session_state.logged_in = False


# UI
st.title("🔐 Streamlit Login System")

if not st.session_state.logged_in:

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(username, password)

else:

    st.success(f"Welcome, {st.session_state.username} 🎉")

    st.write("You are now logged in.")

    if st.button("Logout"):
        logout()
        st.experimental_rerun()