import streamlit as st
import pandas as pd
import os

st.title("👥 Registered Users")

file_name = "users.csv"

if os.path.exists(file_name):

    data = pd.read_csv(file_name)

    if data.empty:
        st.warning("No users registered yet.")
    else:
        st.subheader("User Details")
        st.dataframe(data)

else:
    st.error("Users file not found.")