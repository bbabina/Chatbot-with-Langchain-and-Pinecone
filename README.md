# Chatbot with Langchain and Pinecone

This implements a chatbot that utilizes Sentence Transformation and OpenAI's GPT-3 model to enhance user interactions. The chatbot aims to provide relevant responses to user queries by refining and enhancing their input queries, finding similar sentences using Sentence Transformation, and generating more contextually accurate conversation logs.

### Dependencies

The code uses the following Python libraries:

- `sentence_transformers`: Used to encode input sentences and find similar sentences.
- `pinecone`: Used to create and query an index of similar sentences.
- `openai`: Used to interact with the OpenAI GPT-3 model.
- `streamlit`: Used to create a user-friendly web application for interacting with the chatbot.


## Getting Started

### Installation

To set up the Language Chain Chatbot on your local machine, follow these steps:

1. Create a virtual environment

   ```bash
   virtualenv venv
   venv\Scripts\activate
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain API keys:

   - OpenAI API Key: Get your API key from the OpenAI platform and update it in `main.py` and `utils.py`.
   - Pinecone API Key: Get your API key from the Pinecone platform and update it in `utils.py`.

### Usage

Run the application using the following command:

```bash
streamlit run main.py
```

This will launch a Streamlit application where you can interact with the chatbot.

## Utils Module

### Find Similar Sentences

The `find_match` function in `utils.py` uses SentenceTransformers and Pinecone to find similar sentences in the Pinecone index based on user input.

### Query Refiner

The `query_refiner` function in `utils.py` refines a given query based on a conversation log using the OpenAI GPT-3 model.

### Get Conversation String

The `get_conversation_string` function in `utils.py` generates a formatted conversation log by combining user requests and bot responses.

## Main Module

### Chat Interface

The main functionality of the chatbot is implemented in `main.py`. The script uses OpenAI's GPT-3.5 model for generating conversational responses. It also integrates with the Pinecone index and SentenceTransformers for sentence similarity and embeddings.

Interact with the chatbot by running the Streamlit application and providing queries.
