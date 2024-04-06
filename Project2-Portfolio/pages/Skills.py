import streamlit as st
import pandas
def load_data(filename):
    return pandas.read_csv((filename)+".csv", sep=";")
st.title("Technical Skills")
df = load_data('programminglanguages')


st.header('Programming languages: \n')
col1,col2 =st.columns([2,2])
for index, row in df.iterrows():
    if index%2==0:
        with col1:
            st.info(row['programming languages'])
    else:
        with col2:
            st.info(row['programming languages'])

df = load_data('domainspecs')
st.header('Domain specific skills: \n')
col3,col4 =st.columns([2,2])
for index, row in df.iterrows():
    if index%2==0:
        with col3:
            st.info(row['domain specific skills'])
    else:
        with col4:
            st.info(row['domain specific skills'])




df = load_data('softskills')
st.title('Soft skills: \n')
col5,col6 =st.columns([2,2])
for index, row in df.iterrows():
    if index % 2 == 0:
        with col5:
            st.info(row['soft-skills'])
    else:
        with col6:
            st.info(row['soft-skills'])