import streamlit as st
import pandas as pd
import numpy as np

st.title("Sample Streamlit")

st.write("Something is of with this language")

name = st.text_input("Enter you name : ")
age = st.slider("Enter age : ", 1, 100, 18)

options = ["AD", "CSE", "IT", "ME", "CE" , "ECE", "EEE"]
stream = st.selectbox("Enter the stream : ",options)
df = pd.DataFrame(
    {"haha" : [0, 1, 0, 1],
    "naam" : ["ran", "pan", "tan", "nas"]}
)
st.write(df)
if age < 18:
    st.write(f"hi, {name} is not allowed to take {stream} bcoz he is only {age}")
else:
    st.write("HURRAYY")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
adda = st.sidebar.write("hii")