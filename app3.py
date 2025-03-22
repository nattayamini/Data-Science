import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

# Set up API key
os.environ["GOOGLE_API_KEY"] = "your_api_key"

# Initialize model and memory
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Streamlit UI
st.title("🧠 Conversational AI Data Science Tutor")
st.write("Ask any data science-related question!")

# User input
user_query = st.text_input("You: ", "")

if user_query:
    response = conversation.run(user_query)
    st.write(f"AI Tutor: {response}")
