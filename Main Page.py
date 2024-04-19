import streamlit as st
from st_social_media_links import SocialMediaIcons

st.set_page_config(
    page_title="Amsterdam Annual Consumption Prediction",
    page_icon="👋",
)
social_media_links = [
    "https://www.github.com/dipomari/",
]

'''
# Welcome to Amsterdam Energy Predictor
## This is a simple app that predicts the energy consumption of an apartment in Amsterdam 
### About the project

This project was created as part of the End to End Data Science Project course at GISMA University of Applied Sciences. The goal of this
project is to create a model that can predict the annual electric energy consumption of a household in Amsterdam.
This will be done by using data from the city of Amsterdam.

'''



social_media_icons = SocialMediaIcons(social_media_links)

social_media_icons.render()