import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import google.generativeai as genai
import os

# Set up Google GenAI (Replace 'YOUR_API_KEY' with actual API Key)
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize LangChain with OpenAI model (You can switch to another LLM if needed)
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

def get_travel_options(source, destination):
    """Generate travel options using AI."""
    prompt = f"Find the best travel options from {source} to {destination}, including cabs, trains, buses, and flights with estimated costs."
    response = llm([HumanMessage(content=prompt)])
    return response.content

def main():
    st.title("AI-Powered Travel Planner")
    st.write("Find the best travel options between cities with estimated costs!")
    
    source = st.text_input("Enter Source Location:")
    destination = st.text_input("Enter Destination Location:")
    
    if st.button("Find Travel Options"):
        if source and destination:
            with st.spinner("Fetching travel details..."):
                travel_info = get_travel_options(source, destination)
                st.success("Here are your travel options:")
                st.write(travel_info)
        else:
            st.warning("Please enter both source and destination.")
    
if __name__ == "__main__":
    main()
