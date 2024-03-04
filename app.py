import streamlit as st
import google.generativeai as genai
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Gemini NutriAI 🍽️")

# Sidebar guide
st.sidebar.markdown("""
### Guide
1. Enter your Gemini API key in the provided input field.
2. The default prompt is already integrated into the application.
3. Simply upload a photo of food to receive calorie information.
4. For additional details or a custom prompt, utilize the "Provide Prompt" input to access extra information via the Gemini Vision Pro model.
""")
# Guide for obtaining Google API Key if not available
st.sidebar.subheader("Don't have a Google API Key?")
st.sidebar.write("Visit [Google Makersuite](https://makersuite.google.com/app/apikey) and log in with your Google account. Then click on 'Create API Key'.")

# Configure Google Gemini Pro Vision API with the API key from the input field
api_key = st.sidebar.text_input("Enter your Google API Key:", key="api_key")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("Please enter your Google API Key.")

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our Streamlit app
st.title("Gemini NutriAI 🍽️")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert in nutrition where you need to see the food items from the image
and calculate the total calories, also provide the details of every food items with calories intake
in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
---
---
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input_text)
    st.subheader("The Response is")
    st.write(response)
