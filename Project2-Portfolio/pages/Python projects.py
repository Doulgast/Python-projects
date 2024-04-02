import streamlit as st
import pandas
st.title("Python projects")

col3,empty_col,col4=st.columns([2,0.5,2])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index ,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write("[Source Code](https://github.com/Doulgast/Python-projects)")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write("[Source Code](https://github.com/Doulgast/Python-projects)")