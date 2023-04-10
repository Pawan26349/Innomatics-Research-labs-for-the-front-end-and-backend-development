import streamlit as st

import datetime

import calendar

import numpy as np

import pandas as pd

## start of the heading 

st.title("WELCOME")

st.markdown("<h1 style='text-align: center; color: yellow;'>To My</h1>", unsafe_allow_html=True)

st.markdown('''<h1 style="color:red;text-align:right;font-family: Arial, Helvetica, sans-serif; font-size: 40px; text-transform: uppercase;">APP</h1>''', unsafe_allow_html=True)

## ending of the ending

## starting of the month, year, date tags.

x=list(str(datetime.date.today()).split('-'))

year,month,day=x
year=int(year)
month=int(month)
s1=calendar.monthrange(year,month)

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

days_in_month=s1[1]
year_days=365
if((year%4==0 and year%100!=0) or (year%400==0)):
    year_days+=1;

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Day",day,+days_in_month)    


with col2:
    st.metric("Month",month,+12)

with col3:
    st.metric("Year",year,+year_days)


## end of the month,year  or date.
st.markdown("<hr>",unsafe_allow_html=True)


st.markdown('''<p style="color:lightcoral;letter-spacing: 20px;text-transform: uppercase;font-size: 50px;">the value of time</p>''',unsafe_allow_html=True)
st.write("<br>",unsafe_allow_html=True)


st.write("THAT YOU ALL KNOW THE TIME IS PRESENT IN DIFFERNT FORMS AROUND US .")

st.write("<br>",unsafe_allow_html=True)
st.write("<br>",unsafe_allow_html=True)
st.write("<br>",unsafe_allow_html=True)

cols1,cols2,cols3 = st.columns(3)

with cols1:
    st.write('''<p style="text-align:center;letter-spacing:5px;text-transform:uppercase;font-size:30px;color:red">Multiple time instances</p>''',unsafe_allow_html=True)
    # st.image("https://purepng.com/public/uploads/large/purepng.com-hourglassobjectshourglassclock-watch-glass-time-object-old-hourglass-sand-hour-countdown-timer-sandglass-631522325529dym8u.png",width=200)
    st.write('''<img src="https://purepng.com/public/uploads/large/purepng.com-hourglassobjectshourglassclock-watch-glass-time-object-old-hourglass-sand-hour-countdown-timer-sandglass-631522325529dym8u.png" height="200px" width="200px">''',unsafe_allow_html=True)

with cols2:
    st.write('''<p style="text-align:center;letter-spacing:5px;text-transform:uppercase;font-size:30px;color:red">Multiple time instances</p>''',unsafe_allow_html=True)
    # st.image("https://thumbs.dreamstime.com/b/set-objects-report-time-vectorial-illustration-67312386.jpg",width=200)
    st.write('''<img src="https://thumbs.dreamstime.com/b/set-objects-report-time-vectorial-illustration-67312386.jpg" height="200px" width="200px">''',unsafe_allow_html=True)

with cols3:
    st.write('''<p style="text-align:center;letter-spacing:5px;text-transform:uppercase;font-size:30px;color:red">Carry<br> Watch</p>''',unsafe_allow_html=True)
    # st.image("https://lh5.ggpht.com/Vmm3eP8oYbj60Tj6jN1XnEHCIO29xjXFIr2YwKV32PBbq1JI4RyoEz5E2FrPk097Oe7nU3it2DKvzmxu93L73fw-=s900",width=200)
    st.write('''<img src="https://lh5.ggpht.com/Vmm3eP8oYbj60Tj6jN1XnEHCIO29xjXFIr2YwKV32PBbq1JI4RyoEz5E2FrPk097Oe7nU3it2DKvzmxu93L73fw-=s900" height="200px" width="200px">''',unsafe_allow_html=True)


# st.write('''<img src="https://thumbs.dreamstime.com/b/set-objects-report-time-vectorial-illustration-67312386.jpg" height="200px" width="200px">''',unsafe_allow_html=True)

st.write("<hr>",unsafe_allow_html=True)

st.markdown('''<h2 style="letter-spacing:10px">This is the code for the python language.</h2>''',unsafe_allow_html=True)

st.code('''
from datetime import date
 
# date object of today's date
today = date.today()
 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)''')

st.code('''Output :
2023-02-26''')


st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)

st.write("Month-year chart")
graph=pd.DataFrame(np.random.randn(int(day),int(month)),columns=['year','month'])
st.line_chart(graph)

st.markdown("<hr>",unsafe_allow_html=True)

st.write("Tell me about your self : ")

name=st.text_input("Name")

age=st.number_input("Age")

dob=st.date_input("Date of Birth " )

times=st.time_input("Enter the time you are available for the meet ")

data=st.file_uploader("Here you upload your documents ")

click=st.button("Submit")

if(click == True):
    st.write("the form is submitted .")
    st.balloons()



