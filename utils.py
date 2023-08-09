from sentence_transformers import SentenceTransformer
import pinecone
import openai
import streamlit as st
openai.api_key = ""
model = SentenceTransformer('all-MiniLM-L6-v2')


# initialize Pinecone index
pinecone.init(
    api_key="",  
    environment=""  
)
index = pinecone.Index('langchain-chatbot')


# find similar sentences in the Pinecone index based on user input.
def find_match(input):
    # takes an input sentence and encodes it using the SentenceTransformer model
    input_em = model.encode(input).tolist()

    # queries the Pinecone index to find the most similar matches
    result = index.query(input_em, top_k=2, includeMetadata=True)

    # returns the text of the two most similar matches
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']


# refines a given query based on a conversation log using the OpenAI GPT-3 model
def query_refiner(conversation, query):

    response = openai.Completion.create(
    model="text-davinci-003",

    # conversation --> contains the conversation log, which presumably consists of a series of user queries and bot responses.
    # query --> contains the initial user query that the model should refine 
    prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['text']


# generates a formatted conversation log by combining user requests and bot responses from the session state.
def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string