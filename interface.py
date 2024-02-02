import streamlit as st
from main import mistral_response

st.title('On regarde quoi ce soir ?')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input('Enter your prompt here')

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user', 'content':prompt})
    completion = mistral_response(prompt)

    if completion:
        st.chat_message('assistant').markdown(completion.choices[0].message.content)
        st.session_state.messages.append({'role': 'assistant', 'content': completion.choices[0].message.content})
