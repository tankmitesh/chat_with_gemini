# Inbuild packages
import os 
import warnings
warnings.filterwarnings("ignore")

# Third party package
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Custom packages
from prompt_template import SUMMARY, CODE_ANALYSIS, QUESTION

################################################################################################

def frontend() :

    # set title
    st.title("Chat with : Gemini AI")

    # add dropdown list
    category = st.selectbox("Category", ['Summary', "Question", "Code Anlysis"])

    # add text input
    user_input = st.text_area("Enter your text :")

    # submit button 
    submit_button = st.button("Submit")

    if submit_button :
        # select prompt
        prompt = prompts_data(category)
        prompt = prompt.format(user_input)
        # prompt reponse
        prompt_reponse = llm_chat(prompt)
        
        # show prompt data
        st.write(prompt_reponse)


################################################################################################
    
def llm_chat(text_data: str) -> str :

    # env variables 
    load_dotenv()
    # add config value
    genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
    # defined model
    model = genai.GenerativeModel('gemini-pro')
    # generate text data 
    response = model.generate_content(text_data)
    # format text data
    response = response.text.replace("**", "") 

    return response

################################################################################################

def prompts_data(category: str) -> str :

    if category == "Summary" :
        return SUMMARY
    
    elif category == "Code Anlysis" :
        return CODE_ANALYSIS
    
    elif category == "Question" :
        return QUESTION
    

 