# ### Health Management APP
# from dotenv import load_dotenv

# load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Gemini NutriAI 🍽️")

# Configure Google Gemini API with the API key from the input field
api_key = st.sidebar.text_input("Enter your Google API Key:", key="api_key")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("Please enter your Google API Key.")

# Guide for obtaining Google API Key if not available
st.sidebar.subheader("Don't have a Google API Key?")
st.sidebar.write("Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and log in with your Google account. Then click on 'Create API Key'.")

## Function to load Google Gemini Vision API And get response
def get_gemini_response(input_prompt, image, additional_text=""):
    # Initialize the Gemini model - using the latest model name
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    # If there's additional text from the user, include it
    if additional_text:
        prompt = f"{input_prompt}\n\nAdditional context: {additional_text}"
    else:
        prompt = input_prompt
    
    # Create the content parts - text and image
    contents = [
        {"text": prompt},
        {"inline_data": image}
    ]
    
    # Generate content with the image
    response = model.generate_content(contents)
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        
        # Create an image content part using the appropriate method
        image_part = {"mime_type": uploaded_file.type, "data": bytes_data}
        
        return image_part
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app
st.title("Gemini Health App")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
and calculate the total calories, also provide the details of every food items with calories intake
is below format

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
"""

## If submit button is clicked
if submit:
    try:
        if uploaded_file is None:
            st.error("Please upload an image first.")
        else:
            with st.spinner("Analyzing the image..."):
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_response(input_prompt, image_data, input_text)
                st.subheader("The Response is")
                st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")