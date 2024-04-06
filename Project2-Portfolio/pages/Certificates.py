import streamlit as st
import pandas
def load_data():
    return pandas.read_csv("certificates.csv", sep=";")
st.title("Certificates")


st.header("Udemy certificates")

df = load_data()
col1,emptycol,col2 = st.columns([2.5 , 0.5 , 2.5])

with col1:
    for index, row in df.iterrows():
        if (index % 2 == 0):
            with col1:
                st.header(row["name"])
                st.write(row["url"])
                st.image("images/" + row["image"])
                st.write(row["description"])
        else:
            with col2:
                st.header(row["name"])
                st.write(row["url"])
                st.image("images/" + row["image"])
                st.write(row["description"])


