import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI")

sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student ask any question outside the data science scope, 
                politely decline and tell them to ask the question from data science domain only.
                Always include a helpful statement at the end saying that 
                'In case if your query is not resolved, feel free to click on this link:
                innomatics.in to get in touch with our mentor in a 1:1 zoom call"""

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("Data Science/AI TUTOR")

user_input = st.text_area(label="Enter your query/issue", placeholder="Explain the concept of for loops")

btn_click = st.button("Click Me!")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)