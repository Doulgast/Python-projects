import streamlit as st

from PIL import Image


# Function to set a background image
import streamlit as st

# Function to set a background image


# Set the background image



# Load an image from file
image = Image.open("weather.jpg")
image=image.resize((200,200))
# Display the image
col1,col2 = st.columns([3,1])
with col1:
    st.title("Weather Forecast for the next days")
with col2:
    st.image(image)

place=st.text_input("Please input place...")
days = st.slider("Forecast Days", min_value=1 , max_value=5,help="Slide to the number of days you want to see the forecast for")
option=st.selectbox("Select what data to viw",
                    ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place} .")