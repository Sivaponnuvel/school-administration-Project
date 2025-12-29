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
