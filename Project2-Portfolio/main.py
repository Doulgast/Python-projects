import  streamlit as st
st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("images/doulgas.jpg",width=300)
with col2:
    st.title("Theodoros Doulgarides")

    content=""" Hello, I am Theodoros.\n 
    I have a keen interest in cyber security,ethical hacking and penetration testing.\n
    I am a very hard-working person focused and determined on the targets given to me.I like challenging myself and my skills and I am always eager to learn new things and expand my skillset and knowledge.
    I can easily adapt to new environments,and new objectives given to me. I am a fast learner , with quick thinking and creative problem solving skills. 
    """
    st.info(content)
