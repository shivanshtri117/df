from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

api_key=

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input_text])
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Hindi Transcriber App")

st.header("Hindi Transcriber")
input_text = st.text_area("Paste your paragraph here:", key="input_text", height=300)

# Input prompt for correction
input_prompt = """
You are an expert in Hindi. Your task is to accurately process the provided text according to the following guidelines:

Text preservation: Maintain the original content as much as possible. Make only necessary spelling corrections and minor grammatical adjustments without changing the overall meaning or structure of the text.

Single paragraph format: Ensure that all text is presented in a single paragraph format. Do not break the content into multiple paragraphs or use bullet points.

Number conversion: Convert all numeric values into Hindi words. For example, "100" should be changed to "सौ," "50" to "पचास," etc.

Word translation: When specific words or phrases are requested, provide accurate translations in Hindi. Ensure that the translations are contextually appropriate.

Language consistency: All responses should be in Hindi. Ensure clarity and coherence while adhering to the rules of Hindi grammar.

Context sensitivity: Pay attention to the context in which words or phrases are used, and provide translations or corrections that are relevant to that context.

Handling English words: If any English word is provided (like "and"), write it as "एंड" without translating it.
"""

# When the user presses Enter
if st.button("Get Corrected Response"):
    if input_text.strip():  # Check if the input is not empty
        response = get_gemini_response(f"{input_prompt}\n\n{input_text}")
        st.subheader("Corrected Response:")
        st.write(response)
        # Clear the input text area
        st.session_state.input_text = ""  # Clear the input after processing
    else:
        st.warning("Please paste a paragraph to transcribe.")

# Add an option to clear the input manually
if st.button("Clear Input"):
    st.session_state.input_text = ""  # Clear the input manually
