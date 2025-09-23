from langchain_groq.chat_models import ChatGroq
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.document_loaders import  CSVLoader
# from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS



import warnings
from dotenv import load_dotenv
warnings.filterwarnings("ignore", category=UserWarning)
_=load_dotenv()

CSV_FILE_PATH = "/home/mahavir/code/python_projects/rag_project/backend/data/faq.csv"#"../data/faq.csv"

# initalizing LLM
llm = ChatGroq(model="openai/gpt-oss-20b")

#loading data from csv file
csv_loader = CSVLoader(CSV_FILE_PATH,source_column='prompt',encoding='latin1')
raw_data = csv_loader.load()

# initalizing embedding model
embeddings = HuggingFaceEmbeddings()

# initalizing Vecotr data base 
vector_db = FAISS.from_documents(raw_data,embeddings)

#converting vecotr database into a retreiver
retreiver = vector_db.as_retriever()

#creating chain with retreiver and llm

prompt_template = """Given the following context and a question, generate an answer based on this context only.
In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

CONTEXT: {context}

QUESTION: {question}"""


PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
chain_type_kwargs = {"prompt": PROMPT}



chain = RetrievalQA.from_chain_type(llm=llm,
                            chain_type="stuff",
                            retriever=retreiver,
                            input_key="query",
                            return_source_documents=True,
                            chain_type_kwargs=chain_type_kwargs)


if __name__ == "__main__":
    user_input = input("Ask you question realted to our edtech platform: ")
    response = chain.invoke(user_input)
    
    print('Chat Bot Resposne: ',response['result'])