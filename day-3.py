import streamlit as st
import fitz  
from rank_bm25 import BM25Okapi
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text("text") + "\n"
    return text


def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)


def create_bm25_index(chunks):
    tokenized_chunks = [chunk.lower().split() for chunk in chunks]
    bm25 = BM25Okapi(tokenized_chunks)
    return bm25, chunks


def retrieve_top_chunks(query, bm25, chunks, top_k=3):
    query_tokens = query.lower().split()
    scores = bm25.get_scores(query_tokens)
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
    return "\n".join([chunks[i] for i in top_indices])


st.title(" Monty RAG-Based Machine Learning Bot ")


pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file:
    st.success("PDF uploaded successfully! Now, ask a question.")

   
    text = extract_text_from_pdf(pdf_file)
    chunks = split_text(text)
    bm25, chunks = create_bm25_index(chunks)

  
    query = st.text_input("Ask a question ")

    if query:
        response = retrieve_top_chunks(query, bm25, chunks)
        st.subheader(" Relevant Context:")
        st.write(response)
