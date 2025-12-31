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

def student_signup():
    name,dob,gen=st.columns(3)
    stu_name = name.text_input("Student Name",placeholder="Enter Your Name")
    stu_dob = dob.text_input("Student Date of Birth",placeholder="DD/MM/YYYY")
    gender = gen.selectbox("Gender",["select","Male","Female","Transgender"])

    father,mother,guardian = st.columns(3)
    father_name = father.text_input("Father Name",placeholder="Enter the father name")
    mother_name = mother.text_input("Mother Name",placeholder="Enter the mother name")
    guardian_name = guardian.text_input("Guardian Name",placeholder="Enter the Guardian name")

    mail,ph = st.columns(2)
    email = mail.text_input("E-Mail",placeholder="XXXXXXXX@gmail.com")
    phone = ph.text_input("Phone Number",placeholder="1234567890")

    sat,cit = st.columns(2)
    state = sat.text_input("State","Tamil Nadu")
    city = cit.selectbox("City",["select","Chennai","Tiruvallur","Kancheepuram","Chengalpattu","Vellore","Ranipet","Tirupathur","Tiruvannamalai","Viluppuram","Kallakurichi","Cuddalore","Mayiladuthurai","Nagapattinam","Tiruvarur","Thanjavur","Ariyalur","Perambalur","Tiruchirappalli","Karur","Namakkal","Salem","Dharmapuri","Krishnagiri","Erode","Coimbatore","Tiruppur","Nilgiris","Dindigul","Theni","Madurai","Sivagangai","Ramanathapuram","Virudhunagar","Thoothukudi","Tenkasi","Tirunelveli","Kanyakumari"])

    user,password,password1 = st.columns(3)
    user_name = user.text_input("User Name",placeholder="Create the UserName")
    user_password = password.text_input("Password",placeholder="Create the Password",type="password")
    user_password1 = password1.text_input("Re-Enter password",placeholder="Again Enter the Password",type="password")

    check = st.checkbox("I Agree the Terms and Conditions")
    button = st.button("Sign up")

    if button:
        if not stu_name:
            st.error("Enter the student name")
        
        elif not stu_dob:
            st.error("Fill the Student Date of Birth")

        elif gender == "select":
            st.error("Choose the Gender")

        elif not ((father_name and mother_name) or guardian_name):
            st.error("Enter Father & Mother name OR Guardian name")
        
        elif not email:
            st.error("Enter the E-Mail id")

        elif not phone:
            st.error("Enter the phone number")

        elif not state:
            st.error("Enter the State")

        elif state != "Tamil Nadu":
            st.error("state name is wrong")

        elif city == "select":
            st.error("Choose the city")

        elif not user_name:
            st.error("Enter the User Name") 

        elif not user_password:
            st.error("Enter the password")

        elif not user_password1:
            st.error("Re_Enter the password") 

        elif user_password != user_password1:
            st.error("Re_entered password is Incorrect")
        
        elif check != True:
            st.error("Please accept the terms and conditions")

        else:
            qry = "insert into student(student_name,dob,gender,father_name,mother_name,guardian_name,email,phone_no,city,state,user_name,user_password)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (stu_name,stu_dob,gender,father_name,mother_name,guardian_name,email,phone,city,state,user_name,user_password)
            sd.execute(qry,val)
            con.commit()
            student_id = sd.lastrowid
            st.success("Registration is done")
            st.info(f"Your Roll Number is {student_id}")
            st.balloons()

if selected == "Student" and stu_option == "Signup":

    st.markdown('''
        <div style="text-align: center;">
        <h3>Student Registration Page</h3><div>''',
        unsafe_allow_html=True
        )
    
    st.image("stu_registration.png",width=700)

    student_signup()

