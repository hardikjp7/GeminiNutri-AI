# GeminiNutri-AI [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemininutri-ai.streamlit.app/)

This is a Streamlit web application for the Gemini Health App, which utilizes the Google Gemini Pro Vision API for nutrition analysis. The app takes an input prompt, an image of food items, and calculates the total calories, providing details for each item.



## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/hardikjp7/GeminiNutri-AI.git
   cd GeminiNutri-AI
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

**Default Prompt in Deployed App:**
In the deployed app, there is a default prompt provided below which you can modify on the streamlit site:

```
You are an expert in nutritionist where you need to see the food items from the image
and calculate the total calories, also provide the details of every food item with calories intake
in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
---
---
```


**Note:** For the app to work, you'll need to obtain the Google API key and set it in the `.env` file.

Feel free to explore and analyze nutritional information with the Gemini Health App!
