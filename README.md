# Monty-RAG-Based-Machine-Learning-Bot-

Introduction
This project is a Retrieval-Augmented Generation (RAG) based Q&A bot designed to extract answers from a PDF document without using any AI models or embeddings. It efficiently retrieves relevant information using the BM25 algorithm at the sentence level, ensuring accurate and context-aware answers.
Unlike traditional keyword-based search methods, this approach matches and ranks sentences based on query relevance, providing more precise and meaningful responses. The project is implemented using Streamlit for a user-friendly interface and PyMuPDF for efficient PDF text extraction.
________________________________________
Description
The Q&A bot analyzes the uploaded PDF, indexes its sentences using the BM25 algorithm, and retrieves the most relevant sentences when a user asks a question. The process follows these steps:
1.	PDF Upload & Text Extraction:
o	The bot reads the uploaded PDF and extracts text content.
o	The text is split into individual sentences for better retrieval accuracy.
2.	BM25 Indexing:
o	Each sentence is tokenized and indexed using BM25, a ranking function designed for information retrieval.
o	BM25 assigns relevance scores to sentences based on how well they match the user’s question.
3.	Query Processing & Answer Retrieval:
o	When a user enters a query, the bot compares it with indexed sentences.
o	It retrieves the top-ranked sentences that best answer the question.
4.	Displaying Results:
o	The bot presents the retrieved sentences in a clear and readable format on the Streamlit interface.
This approach ensures that answers are contextually relevant without requiring any AI-based language models, making the system lightweight, fast, and easy to use.
________________________________________
Required Tools & Libraries
To implement this project, the following tools and Python libraries are required:
•	Python (3.x) – Primary programming language
•	Streamlit – For building an interactive web UI
•	PyMuPDF (fitz) – For extracting text from PDFs
•	Rank-BM25 – For sentence-level retrieval and ranking
•	Regex (re) – To split text into sentences for better matching
________________________________________
Retrieval-Augmented Generation (RAG) in This Project

•	This project utilizes Retrieval-Augmented Generation (RAG), but instead of using AI-based generation models, it relies solely on retrieval techniques to fetch the most relevant sentences from a PDF document. Below are the key components of the RAG approach used in this project:
________________________________________
	Retrieval Mechanism

•	The retrieval process is handled using the BM25 algorithm, which is a ranking function used in information retrieval. The workflow includes:
•	 PDF Text Extraction – Extracts text from the uploaded PDF.
 Sentence-Level Indexing – Splits the text into sentences rather than paragraphs to improve answer precision.
 BM25 Ranking – Assigns scores to sentences based on their relevance to the user’s query.
Top Sentence Selection – Returns the most relevant sentences as answers.
•	By using sentence-based retrieval, the bot ensures that users receive concise and accurate responses rather than entire document chunks.

________________________________________

2. Augmenting Information (Without AI Models)

•	Unlike traditional RAG systems that use deep learning models (e.g., GPT or BERT) to generate responses, this project enhances retrieval by:
•	✔ Using BM25 to find the most relevant answer without embeddings
✔ Providing multiple relevant sentences instead of a single static answer
✔ Allowing users to refine questions for better retrieval
•	This makes the system faster, more transparent, and explainable, as it only retrieves information directly from the document without altering it.
________________________________________
3. Why This RAG Approach Works Well Here

•	 No Need for Expensive AI Models – Works without transformers or deep learning models.
 Lightweight and Fast – Only requires sentence tokenization and ranking.
More Accurate Retrieval – Unlike chunk-based methods, it finds exact sentences that match the query.
Better for Structured PDFs – Works well with research papers, legal documents, and reports.
