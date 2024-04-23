import streamlit as st

from PIL import Image
import plotly.express as px

# Function to set a background image
import streamlit as st
from backend import get_data
# Function to set a background image


# Set the background image



# Load an image from file
image = Image.open("images/weather.jpg")
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
if place:
    try:
        filtered_data=get_data(place,days)
        if option == "Temperature":
            temperatures= [dict["main"]["temp"] /10 for dict in filtered_data]

            dates=[dict["dt_txt"] for dict in filtered_data  ]
            figure=px.line(x =dates ,y=temperatures,labels={"x":"Date", "y": "Temperature in Celcius"})
            st.plotly_chart(figure)
        if option=="Sky":
            images= {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                     "Snow": "images/snow.png"}

            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths=[images[condition]for condition in sky_conditions]
            st.image(image_paths,width=115)

    except KeyError:
        st.write("That place does not exist.")