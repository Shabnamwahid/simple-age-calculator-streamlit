import streamlit as st
from datetime import datetime
import time  # ⏳ Delay ke liye 

# 🎨 Custom CSS for Readability
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.pexels.com/photos/5192095/pexels-photo-5192095.jpeg?auto=compress&cs=tinysrgb&w=1920&h=1080&dpr=2');
        background-size: cover;
        background-position: center;
    }
    .title { color: white; text-align: center; font-size: 3em; font-weight: bold; }
    .subheading { color: white; text-align: center; font-size: 1.5em; }
    .age-text { color: white; font-size: 20px; font-weight: bold; }
    .years-left { color: white; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# 🎂 Title
st.markdown('<h1 class="title">🎂 Simple Age Calculator</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheading">Find Out Your Age & More!💖</h2>', unsafe_allow_html=True)

# 📅 User Input Without Auto-slash
dob = st.text_input("Enter Your Birthdate (DD/MM/YYYY):", max_chars=10)

if len(dob) == 10:
    try:
        birth_date = datetime.strptime(dob, "%d/%m/%Y")
        today = datetime(2025, 3, 17)  # Fixed current date

        # ✅ Correct Age Calculation
        age = today.year - birth_date.year
        if today < datetime(today.year, birth_date.month, birth_date.day):
            age -= 1

        # 🎯 Years Left for 100
        years_left = 100 - age

        # 🎉 Display Result
        st.markdown(f'<p class="age-text">You are {age} years old. 🎉</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="years-left">You have {years_left} years left until you turn 100. 🎯</p>', unsafe_allow_html=True)
        
        # ⏳ 2-second delay
        time.sleep(2)

        # 🎈 Balloons Animation
        st.balloons() 

    except ValueError:
        st.error("Please enter a valid date in DD/MM/YYYY format!")

    st.write("Built with ❤️ by Shabnam Wahid!")