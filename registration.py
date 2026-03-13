import streamlit as st
import csv
import os

st.title("📝 User Registration")

file_name = "users.csv"

# Create file if it doesn't exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Email", "Password"])


username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")


if st.button("Register"):

    if username == "" or email == "" or password == "":
        st.warning("Please fill all fields")

    elif password != confirm_password:
        st.error("Passwords do not match")

    else:

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, email, password])

        st.success("Registration Successful!")