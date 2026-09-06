"""
Lesson 31: Retrieval-Augmented Generation (RAG) Basics

Demonstrates the core RAG architecture: retrieve relevant documents
via semantic search, then feed them to an LLM as context so it
answers grounded in real data rather than just its training
knowledge. Uses TF-IDF for retrieval (works locally on Termux); a
production system would use real neural embeddings (Lesson 30) via
a vector database - this is the same architecture used in the
user's own Termux AI project's evidence-pack/RAG system.
"""

import os
from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

knowledge_base = [
    "The Termux AI project runs on an Android phone with 8 CPU cores and about 3GB of usable RAM.",
    "The project uses Groq for fast responses to Somali and Arabic questions, since on-device translation isn't feasible.",
    "Local inference uses llama.cpp with a Qwen2.5-1.5B model, achieving about 7.69 tokens per second generation speed.",
    "SearXNG is used as a self-hosted search engine to avoid depending on paid search APIs.",
    "The project's router.py handles rate limiting, since Groq's free tier allows only 8000 tokens per minute.",
]


def retrieve_relevant_docs(query: str, documents: list[str], top_n: int = 2) -> list[str]:
    """Find the most relevant documents to a query using TF-IDF + cosine similarity."""
    vectorizer = TfidfVectorizer()
    all_texts = documents + [query]
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    query_vector = tfidf_matrix[-1]
    doc_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(query_vector, doc_vectors)[0]
    top_indices = similarities.argsort()[::-1][:top_n]

    return [documents[i] for i in top_indices]


def answer_with_rag(query: str) -> str:
    """Full RAG pipeline: retrieve relevant context, then ask the LLM using it."""
    relevant_docs = retrieve_relevant_docs(query, knowledge_base)
    context = "\n".join(relevant_docs)

    prompt = f"""Answer the question using ONLY the context below. If the context doesn't contain the answer, say so.

Context:
{context}

Question: {query}"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )
    return response.choices[0].message.content


question = "How fast is the local model on the phone, and why is Groq used instead for some languages?"

print(f"Question: {question}\n")
print("Retrieved context:")
for doc in retrieve_relevant_docs(question, knowledge_base):
    print(f"- {doc}")

print("\nRAG-grounded answer:")
print(answer_with_rag(question))
