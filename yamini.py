import openai
import streamlit as st

# Set up OpenAI API Key
client = openai.OpenAI(api_key="your_openai_api_key")
def review_code(user_code):
    """Send user code to OpenAI API for bug detection and fixes."""
    prompt = f"Review the following Python code, detect errors, and suggest improvements:\n\n{user_code}\n\nProvide fixed code:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

# Streamlit UI
st.title("🧑‍💻 AI Code Reviewer")

st.write("Submit your Python code for review and receive bug reports with fixes.")

# Code input area
user_code = st.text_area("Paste your Python code here:", height=200)

if st.button("Review Code"):
    if user_code.strip():
        with st.spinner("Analyzing your code..."):
            reviewed_code = review_code(user_code)
        
        # Display reviewed output
        st.subheader("🔍 AI-Generated Code Review & Fixes")
        st.code(reviewed_code, language="python")
    else:
        st.warning("⚠ Please enter some Python code.")
