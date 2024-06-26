import streamlit as st
import sys
sys.path.append("Project2-Portfolio/send_email.py")
from send_email import send_email
col1,col2=st.columns([2 , 2])
with col1:
    st.header("Contact Me")
with col2:
    st.image("images/contactme.jpg",width=200)

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    # Define options for the dropdown
    options = ['Jobs', 'Project proposals', 'Other']

    # Add the dropdown to the Streamlit app
    selected_option = st.selectbox('Select an option:', options)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: {selected_option} - Website Contact
Email sent from: {user_email}
Message: {raw_message}
            
    """
    button = st.form_submit_button("Submit message")

    if button:

        print("I was pressed")
        send_email(message)
        st.info("Your message was sent succesfully. Please wait for an answer.")