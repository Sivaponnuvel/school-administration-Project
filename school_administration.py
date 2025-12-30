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

if selected == "Home page":
    st.markdown('''
        <div style="text-align: center;">
            <h3>Welcome to  Our ABC School </h3>
        </div>''',
     unsafe_allow_html=True
    )

    st.markdown('''
      <div style="text-align: center;">
         <h6>School administration is a smart online solution that simplifies the management of students, teachers, and school operations</h6>
      </div>''',
     unsafe_allow_html=True
    )   

    st.image("school_administration.png",caption="ABC School",width=710)

    st.markdown("-------") 
    st.header("🏆 School Highlights")
    st.subheader("Achievements and important activities")
    st.write("⭐⭐⭐⭐⭐ 100% pass result in board examinations")
    st.write("⭐⭐⭐⭐ Active student participation in academics & sports")
    st.write("⭐⭐⭐⭐⭐Well-organized teaching and learning environment")
    st.write("© 2026 Admissions Are Open")

