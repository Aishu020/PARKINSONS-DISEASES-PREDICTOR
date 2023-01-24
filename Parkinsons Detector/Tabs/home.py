"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Parkinson's Disease Predictor")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.
            This Web application will help you to predict whether a person has a risk of being a patient of Parkinson's disease or has the disease in minor or acute level.This app helps to predict the causes for such pathological scenarios in future by analysing the values of several features using the Random Forest Classifier.
        </p>
    """, unsafe_allow_html=True)