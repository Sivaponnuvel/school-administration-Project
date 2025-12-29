import mysql.connector
from tabulate import tabulate
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

con = mysql.connector.connect(
        host="localhost",
        username="root",
        password="siva2025",
        database="school_administration"
)
sd = con.cursor()

st.sidebar.title("School Administration")

with st.sidebar:
    selected = option_menu("Main Menu",["Home page","Student","Teacher"])

    if selected == "Student":
        st.sidebar.title("Student")
        stu_option = option_menu("",["Signup","Login"])

    elif selected == "Teacher":
        st.sidebar.title("Teacher")
        tec_option = option_menu("",["Signup","Login"])
