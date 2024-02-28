from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


API_KEY = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY,transport='rest')


## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image):
    if input!= "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    
    return response.text


##Initialze streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header('Gemini Application')
input=st.text_input("Input Prompt:", key ="input")
uploaded_file = st.file_uploader("Choose an image:",type=['jpg','png','jpeg'])
image =""

if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image',use_column_width= True)

submit =st.button("Tell me something about Image")

## if ash button is clicked 
    
if submit:

    response = get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)
    