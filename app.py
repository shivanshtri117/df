from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key="AIzaSyAVdMsVX_vqD03IzE0c92dGrG4BSNrq6RU")

def get_gemini_response(input_text):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([input_text])
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Initialize our Streamlit app
st.set_page_config(page_title="Hindi Transcriber App")
st.header("Hindi Transcriber")

# Add description
st.markdown("""
This app helps you transcribe and correct Hindi text. It will:
- Fix spelling and grammar
- Convert numbers to Hindi words
- Format text into a single paragraph
- Handle English words appropriately
""")

# Text input area
input_text = st.text_area("Paste your paragraph here:", key="input_text", height=300)

# Input prompt for correction
input_prompt = """
You are an expert in Hindi. Your task is to accurately process the provided text according to the following guidelines:
Text preservation: Maintain the original content. Make only necessary spelling corrections without changing the overall meaning or structure of the text.
Single paragraph format: Ensure that all text is presented in a single paragraph format. Do not break the content into multiple paragraphs or use bullet points.
Number conversion: Convert all numeric values into Hindi words. For example, "100" should be changed to "सौ," "50" to "पचास," etc.
Word translation: When specific words or phrases are requested, provide accurate translations in Hindi. Ensure that the translations are contextually appropriate.
Language consistency: All responses should be in Hindi. Ensure clarity and coherence while adhering to the rules of Hindi grammar.
Context sensitivity: Pay attention to the context in which words or phrases are used, and provide translations or corrections that are relevant to that context.
Handling English words: If any English word is provided (like "and"), write it as "एंड" without translating it.
"""

# Create two columns for buttons
col1, col2 = st.columns(2)

# Process button
with col1:
    if st.button("Get Corrected Response", type="primary"):
        if input_text.strip():  # Check if the input is not empty
            with st.spinner("Processing your text..."):
                response = get_gemini_response(f"{input_prompt}\n\n{input_text}")
                st.subheader("Corrected Response:")
                st.write(response)
        else:
            st.warning("Please paste a paragraph to transcribe.")

# Clear button
with col2:
    if st.button("Clear Input"):
        st.session_state.input_text = ""
        st.experimental_rerun()

# Add footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Google Gemini-Pro")
