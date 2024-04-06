import  streamlit as st
import pandas
st.set_page_config(layout="wide")
# Define column widths


# Create columns with specified widths
col1,  mid_col,col2 = st.columns([1.5,0.5,2])

with col1:
    st.image("images/doulgas.jpg",width=300)
    st.info("Languages: \n"
            "\nGreek\n"
            "\nEnglish\n"
            "\nRussian")
with col2:
    st.title("Theodoros Doulgarides")
    st.header("A little about myself.")
    content=""" Hello, I am Theodoros.\n 
    I have a keen interest in cyber security,ethical hacking and penetration testing.\n
    I am a very hard-working person focused and determined on the targets given to me.I like challenging myself and my skills and I am always eager to learn new things and expand my skillset and knowledge.
    I can easily adapt to new environments,and new objectives given to me. I am a fast learner , with quick thinking and creative problem solving skills. 
    """
    st.info(content)
    st.header("Personal info")
    content2= """•	Date of Birth: 18 AUGUST 2000\n
•	Nationality: Greek\n
•	Email: theodorosdoulgarides@gmail.com & doulgastgk@outlook.com \n
•	Contact phone: +357 97735393 \n
•	Address: Troias 24, Aglantzia, Nicosia , 2103  \n
•	LinkedIn: www.linkedin.com/in/theodoros-doulgarides-0185b9292 \n
•	Github: https://github.com/Doulgast\n
"""
    st.info(content2)
    content3 = """ This is my website. Here you can find all my information , my certificates and my projects.
    Feel free to contact me. 
    """
    st.write(content3)


