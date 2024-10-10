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
input_prompt = prompt = """
You are an expert in Hindi, tasked with processing text according to the following guidelines. Ensure to maintain the integrity of the original content while making necessary adjustments.Follow all these instructions, don't write anything on behlaf of yourself

Instructions:

1. Text Preservation:  
   Maintain the original content. Make only necessary spelling corrections without altering the overall meaning or structure of the text.

2. Single Paragraph Format:  
   Present all text in a single paragraph. Avoid breaking the content into multiple paragraphs or using bullet points.

3. Number Conversion:  
   Convert all numeric values into Hindi words. For example, change "100" to "सौ" and "50" to "पचास."

4. Word Handling:  
   When specific English words are present, write them in Hindi script without translating. For example, write "birds" as "बर्ड्स."

5. Language Consistency:  
   All responses must be in Hindi. Ensure clarity and coherence while following Hindi grammar rules.

6. Context Sensitivity:  
   Pay attention to the context of words or phrases, providing translations or corrections that are relevant.

7. Handling English Words:  
   For any English words provided (like "and"), write them as "एंड" without translation.

Compliance Requirement:  
Adhere to all these guidelines strictly for effective fine-tuning.
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


