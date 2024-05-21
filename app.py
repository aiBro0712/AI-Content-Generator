
import streamlit as st 
import os
import google.generativeai as genai
from api_key import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)


#layout setting 
st.set_page_config(layout="wide")
 
 #our blog title
st.title('AI Content generator for Your blog')

#sub header app
st.subheader('Blog craft for perfect aAi blog companion')

#side bar for user input
with st.sidebar:
    st.title('Input your blog details')
    st.subheader('Enter details of the blog you want generate')

    #blog title 
    blog_title = st.text_input('Enter the title your blog')

    #blog keyword input  
    blog_keywords = st.text_area("Keywords (comma-separated)")
    


    #number of words 
    num_words = st.slider("Number of words",min_value=250,max_value=1000,step=100)

    #number of images 
    # num_imgs = st.number_input('enter number images for blog',min_value=1,max_value=5,step=1)
    sb_button = st.button('Generate blog')
    promt_parts =[
         f"Generate a comprehensive, engaging blog post relevant to the given the \"{blog_title}\" and keywords \"{blog_keywords}\". blog should be approximately {num_words} words length , suitable for online audience . ensure the  content is original ,informative and maintain a consistent tone through.",
         ]

    #submit button for generate blog
if sb_button:
         response = model.generate_content(promt_parts)
         st.write(response.text)
        
