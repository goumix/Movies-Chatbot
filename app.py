# from langchain_community.document_loaders import LocalDocumentLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import streamlit as st

# Give app title
st.title('Chatbot')

# Build a prompt input template to display the prompt
prompt = st.chat_input('Enter your prompt here')

#if the user hits enter, then 
if prompt: 
    #display the prompt
    st.chat_message('user').markdown(prompt)
