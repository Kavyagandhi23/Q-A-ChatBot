from langchain.llms import OpenAI 
from dotenv import load_dotenv
import os 
import streamlit as st

load_dotenv()

# Function to define OpenAI model
def openai_response(question):
    llm = OpenAI(temperature=0.7, openai_api_key=os.getenv('OPEN_API_KEY'), model_name='text-davinci-003')
    response=llm(question)
    return response

# Initialize Streamlit app

st.set_page_config(page_title="Langchain Application")
st.header('Q&A ChatBot')

input = st.text_input("Input: ", key="input")
response=openai_response(input)

submit=st.button('Generate Response')

if submit:
    st.subheader('AI Response:')
    st.write(response)


