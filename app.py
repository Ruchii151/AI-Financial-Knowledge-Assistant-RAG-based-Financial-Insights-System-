# AI Financial Report Analyzer
import streamlit as st

import os 

from langchain_google_genai import ChatGoogleGenerativeAI 

#RAG Pipeline
from langchain_community.document_loaders import WebBaseLoader #Document_Loader
from langchain_text_splitters import RecursiveCharacterTextSplitter #Text_splitter
from langchain_ollama import OllamaEmbeddings #Embeddings


from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma
import time
from bs4 import SoupStrainer


from dotenv import load_dotenv
load_dotenv()

# Load the Google Gemini API key 
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

urls = [
    "https://en.wikipedia.org/wiki/Systematic_investment_plan",
    "https://www.investopedia.com/terms/s/systematicinvestmentplan.asp",
    "https://www.investopedia.com/articles/mutualfund/08/systematic-investment-plan.asp",
    "https://en.wikipedia.org/wiki/Mutual_fund",
    "https://en.wikipedia.org/wiki/Investment"
]

if "vectors" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="nomic-embed-text")
    # LOAD
    st.session_state.loader = WebBaseLoader(urls,bs_kwargs=dict(parse_only=SoupStrainer(["p"])))
    st.session_state.docs = st.session_state.loader.load()
    # ✅ CLEAN (AFTER docs is created)
    st.session_state.docs = [doc for doc in st.session_state.docs if len(doc.page_content.strip()) > 200]
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap=200)
    
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
    st.session_state.vectors = Chroma.from_documents(st.session_state.final_documents,st.session_state.embeddings)
    
    
st.title("Financial knowledge RAG assistant")

llm_brain = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

finance_prompt = ChatPromptTemplate.from_template(
"""
You are a financial analysis assistant that helps interpret company financial reports.

Use ONLY the provided context to answer the question.

Context:
{context}

Question:
{input}

Instructions:
- Identify key financial insights from the documents.
- Focus on revenue, profit, risks, and business performance when relevant.
- Summarize the information clearly and professionally.
- If the context does not contain the answer, say:
  "The financial documents provided do not contain this information."
- Provide concise insights rather than long explanations.

Answer:
"""
)
document_chain = create_stuff_documents_chain(llm_brain,finance_prompt)
retriever = st.session_state.vectors.as_retriever(search_kwargs={"k": 5})
retrieval_chain = create_retrieval_chain(retriever,document_chain)

prompt = st.text_input("Input Your Prompt here")

if prompt: 
    start = time.process_time()
    response = retrieval_chain.invoke({"input":prompt})
    print("Response_Time", time.process_time()-start)
    st.write(response['answer'])
    
    #With a streamlit expander 
    with st.expander("Document Similarity Search"):
        #Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------------")
            
            
            
            
            
            