import streamlit as st 
from Langchain_config import llm_chain, get_summary
st.title('News Research Tool')
st.write('Enter your query to get the latest news articles summarized')
query=st.text_input('query')
if st.button('Get News'):
    if query:
        summaries=get_summary(query)
        response=llm_chain.run({'query':query,'summaries':summaries})
        st.write('summary')
        st.write(response)
    else:
        st.write('Please enter a querry.')