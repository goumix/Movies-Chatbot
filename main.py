from openai import OpenAI
from langchain.document_loaders import CSVLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

db = ''
docs = ''

def initialize_vector_db(prompt):
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    loader = CSVLoader("movies.csv")
    documents = loader.load()
    db = Chroma.from_documents(documents, embedding_function)
    docs = db.similarity_search(prompt)
    print(docs[0])
    return docs[0]


def mistral_response(prompt):
    docs = initialize_vector_db(prompt)
    completion = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": f"You are a movie expert. Your database return this film : {docs}"},
        {"role": "user", "content": prompt}
    ],
    temperature=0.5,
    )
    print(completion.choices[0].message.content)
    return completion
