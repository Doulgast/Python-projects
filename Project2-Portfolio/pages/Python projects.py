import streamlit as st
import pandas
st.title("Python projects")
def load_data():
    return pandas.read_csv("data.csv", sep=";")

col3,empty_col,col4=st.columns([2.5,0.5,2.5])
df = load_data()

with col3:
    for index ,row in df.iterrows():
        if(index%2==0):
            with col3:
                st.header(row["title"])
                st.write(row["description"])
                st.image("images/"+row["image"])
                st.write("[Source Code](https://github.com/Doulgast/Python-projects)")
        else:
            with col4:
                st.header(row["title"])
                st.write(row["description"])
                st.image("images/" + row["image"])
                st.write("[Source Code](https://github.com/Doulgast/Python-projects)")
# with col4:
#     for index,row in df[10:].iterrows():
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image("images/"+row["image"])
#         st.write("[Source Code](https://github.com/Doulgast/Python-projects)")