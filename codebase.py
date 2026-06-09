import streamlit as st
import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader,TextLoader
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain_classic.retrievers import BM25Retriever,EnsembleRetriever
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_classic.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory


st.set_page_config(page_title="Codebase",layout="wide")
st.title("🧠 CodeMind AI")
st.caption("Understand, Search & Chat with Your Codebase")


with st.sidebar:
    st.header("Settings")
    groq_ap = st.text_input("Groq API Key",type='password')
    load_btn = st.button("Load Codebase")
    st.markdown("---")
    st.markdown("""
    ## 🚀 Features
    - 📂 Load Entire Python Codebase
    - 🧠 AI-Powered Code Understanding
    - 🔍 Hybrid Search
    - 💬 Chat With Your Code
    - 🧾 Explains Functions & Files
    - 🧠 Memory Support
    - ⚡ Chroma Vector Database
    - 🤖 Groq LLM Integration
    """)

    st.markdown("---")
    st.markdown("Built with ❤️ using LangChain")

if 'store' not in st.session_state:
    st.session_state.store={}
if 'session_id' not in st.session_state:
    st.session_state.session_id=str(uuid.uuid4())
def get_session_history(session_id: str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id]=InMemoryChatMessageHistory()
    return st.session_state.store[session_id]

def load_codebase():
    loader=DirectoryLoader(
        path='codebase',
        glob='**/*.py',
        loader_cls=TextLoader
    )
    return loader.load()


if load_btn and groq_ap:
    with st.spinner("Loading......."):
        docs=load_codebase()
        split=RecursiveCharacterTextSplitter.from_language(language='python',chunk_size=800,chunk_overlap=300)
        chunks=split.split_documents(docs)
        embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectordb=Chroma.from_documents(chunks,embeddings,persist_directory='chromas_db')
        dense_retreiver=vectordb.as_retriever(search_kwargs={'k':4})
        bm=BM25Retriever.from_documents(chunks)
        bm.k=4
        hyb=EnsembleRetriever(retrievers=[dense_retreiver,bm],weights=[0.5,0.5])
        prompt=ChatPromptTemplate.from_messages([
("system","You are a senior software engineers." 
"Answer questions about the codebase clearly ."
"Mention file names and functions when possible."
),
('human',"use the following code context to answer the question:\n\n" "{context}\n\n" "Question:{input}")
        ])
        
        llm = ChatGroq(
            api_key=groq_ap,
            model="openai/gpt-oss-120b"
        )
        doc_chain=create_stuff_documents_chain(llm,prompt)
        retreival_ch=create_retrieval_chain(hyb,doc_chain)

        st.session_state.chatbot=RunnableWithMessageHistory(
            retreival_ch,
            get_session_history,
            input_messages_key='input',
            history_messages_key='chat_history',
            output_messages_key='answer'
        )
        st.success("Codebase indexed succefully ")

if 'chatbot' in st.session_state:
    user=st.chat_input("Ask about the code .......")
    if user:
        response=st.session_state.chatbot.invoke(
            {
                'input':user
            },
            config={'configurable':{'session_id':st.session_state.session_id}}
        )
        st.chat_message("user").write(user)
        st.chat_message("assistant").write(response['answer'])
else:
    st.info("Enter  groq api ky and click 'load base'")





