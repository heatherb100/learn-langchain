import openai
import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

st.header('🔗 Chains')

st.write('''
Now that we have a good understanding of LLMs and Prompt Templates, we are ready to
introduce chains, the most important core component of LangChain. Chains are pre-built
classes that allow us to combine LLMs and Prompts together, with a modular approach
designed to facilitate the creation of complex language processing pipelines while
keeping our codebase solid and readable.

LangChain provides chains for the most
common operations (routing, sequential execution, document analysis) as well as
advanced chains for working with custom data, handling memory and so on. Also, we
will see more advanced LangChain features (tokenizers, transformers, embeddings)
that are much easier to use with chains.
''')

st.subheader('Our first basic Chain')

st.code('''
llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.9)

prompt = ChatPromptTemplate.from_template("I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}? The name should honor the film story as it is. Please limit your answer to the name only.")

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run(movie)
''')

openai_key = st.text_input("OpenAI Api Key")

with st.form("basic_chain"):

    movie = st.text_input("Movie", placeholder="The Green Mile")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

    	with st.spinner('Processing your request...'):

	        llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.9)

	        prompt = ChatPromptTemplate.from_template('''
	        I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}?\
	        The name should honor the film story as it is. Please limit your answer to the name only.\
	        If you don't know the movie, answer: "I don't know this movie"
	        ''')

	        chain = LLMChain(llm=llm, prompt=prompt)

	        response = chain.run(movie)

	        st.code(response)

st.write('''
This basic Chain is not very different from the Prompt Template approach, but let's move forward to
some more complex example where we can explore the adavntages and the simplicity that chains bring us.
''')

st.subheader('Sequential Chain')