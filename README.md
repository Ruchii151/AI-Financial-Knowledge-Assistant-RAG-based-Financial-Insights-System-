# AI-Financial-Knowledge-Assistant-RAG-based-Financial-Insights-System-

An intelligent Retrieval-Augmented Generation (RAG) system designed to streamline the process of understanding and analyzing financial concepts from multiple web-based sources. This application enables users to query financial topics and receive accurate, context-aware responses grounded in relevant source content.

---

## Problem Statement

Understanding financial concepts such as investments, mutual funds, and systematic investment plans requires referring to multiple resources. This process is often inefficient, lacks structured retrieval, and makes it difficult to extract concise insights quickly.

---

## Solution Overview

This project introduces an AI-powered assistant that leverages Retrieval-Augmented Generation (RAG) to process financial content from multiple web sources and provide precise answers. It combines semantic search with Large Language Models (LLMs) to deliver high-quality, context-driven responses.

---

## System Architecture

User Query
↓
Web Document Loader (URLs)
↓
Text Cleaning & Filtering
↓
Text Chunking
↓
Embedding Generation
↓
Vector Database (ChromaDB)
↓
Retriever (Top-K Similar Chunks)
↓
LLM (Gemini - Answer Generation)
↓
Final Answer with Context

---

## Core Features

- Multi-source financial question answering
- Semantic search using vector embeddings
- Context-aware response generation using LLMs
- Focused financial insights (investment concepts, risks, strategies)
- Transparent retrieval with document similarity display
- Real-time interaction using Streamlit

---

## Technology Stack

Framework: LangChain
Vector Database: ChromaDB
Embeddings: Ollama (nomic-embed-text)
LLMs: Google Gemini (gemini-2.5-flash)
Frontend: Streamlit
Language: Python
Concepts: NLP, Semantic Search, RAG

---

## Workflow Explanation

### 1. Data Ingestion

The system collects financial content from multiple web sources using a document loader.

### 2. Data Cleaning

Short or irrelevant text content is filtered out to improve retrieval quality.

### 3. Text Processing

The cleaned content is split into smaller chunks using a recursive text splitter.

### 4. Embedding Generation

Each chunk is converted into dense vector representations using Ollama embeddings.

### 5. Vector Storage

Embeddings are stored in ChromaDB for efficient similarity-based retrieval.

### 6. Retrieval

Relevant chunks are retrieved based on semantic similarity to the user query.

### 7. Response Generation

The retrieved context is passed to a Gemini LLM with a structured prompt to generate concise financial insights.

### 8. Output Visualization

The final response is displayed along with retrieved document chunks for transparency.

---

## Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/Ruchii151/ai-financial-assistant.git
cd ai-financial-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

```bash
GOOGLE_API_KEY=your_api_key
```

### 4. Run Application

```bash
streamlit run app.py
```

---

## Example Use Cases

- Understand financial concepts such as SIP, mutual funds, and investments
- Compare different investment strategies
- Summarize financial topics from multiple sources
- Identify risks and benefits of financial approaches

---

## Impact

This system reduces the time required to understand financial concepts by providing instant, structured insights from multiple sources. It demonstrates the practical implementation of RAG for domain-specific knowledge retrieval.

---

## Future Enhancements

- Support for PDF-based financial reports
- Integration with real financial datasets
- Extraction of structured financial metrics (revenue, profit, ratios)
- Hybrid search (keyword + semantic search)
- Cloud deployment for scalability

---

## Conclusion

The AI Financial Knowledge Assistant demonstrates the application of Retrieval-Augmented Generation in the financial domain by combining semantic search, vector databases, and LLMs. It highlights the ability to design domain-specific AI assistants for efficient knowledge retrieval.


