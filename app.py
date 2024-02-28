

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


import google.generativeai as genai

API_KEY = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY,transport='rest')


## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


##initialize  streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
   
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)