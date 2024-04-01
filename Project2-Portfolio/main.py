import  streamlit as st
st.set_page_config(layout="wide")
# Define column widths
col1_width = 1
col2_width = 3

# Create columns with specified widths
col1, col2 = st.columns([col1_width, col2_width])

with col1:
    st.image("images/doulgas.jpg",width=300)
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
    content3 = """ Below you can find some projects that i have worked on a,certificates and areas of research. \n
    Feel free to contact me.
    """
    st.write(content3)