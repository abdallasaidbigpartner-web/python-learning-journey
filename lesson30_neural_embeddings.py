"""
Lesson 30: Real Neural Embeddings & Semantic Search

Demonstrates true neural embeddings (via sentence-transformers) for
semantic search - unlike TF-IDF (Lesson 29), this captures actual
meaning, correctly matching conceptually related text even without
shared words. This is the real mechanism behind modern RAG systems,
including the architecture used in the user's own Termux AI project.

Run via GitHub Actions cloud CI since sentence-transformers requires
PyTorch, which cannot build on Termux/Android.
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Machine learning models learn patterns from data",
    "Neural networks are inspired by the human brain",
    "Python is a popular programming language for data science",
    "The weather today is sunny and warm",
    "Deep learning uses layers of neurons to process information",
]

query = "How do AI models learn from information?"

model = SentenceTransformer("all-MiniLM-L6-v2")

document_embeddings = model.encode(documents)
query_embedding = model.encode([query])

similarities = cosine_similarity(query_embedding, document_embeddings)[0]

print(f"Query: {query}\n")
print("Documents ranked by TRUE semantic relevance:")
ranked_indices = similarities.argsort()[::-1]
for idx in ranked_indices:
    print(f"Score {similarities[idx]:.3f}: {documents[idx]}")
