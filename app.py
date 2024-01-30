# from langchain_community.document_loaders import LocalDocumentLoader
import langchain
from sqlalchemy.engine import URL
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import watson
import sys
sys.path.append("/opt/anaconda3/lib/python3.9/site-packages")exit 
import streamlit as st

# Give app title
st.title('On regarde quoi ce soir ?')

# Setup a session state message variable to hold all the old messages 
if 'messages' not in st.session_state:
    st.session_state.messages = []

#Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Build a prompt input template to display the prompt
prompt = st.chat_input('Enter your prompt here')

#if the user hits enter, then 
if prompt: 
    #display the prompt
    st.chat_message('user').markdown(prompt)
    #store the user prompt in state
    st.session_state.messages.append({'role':'user', 'content':prompt})


