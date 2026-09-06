"""
Lesson 29: Semantic Search with TF-IDF & Cosine Similarity

Demonstrates the classic (pre-neural-network) approach to semantic
search: converting text into numerical vectors (TF-IDF) and measuring
similarity between them (cosine similarity) - the conceptual ancestor
of modern embedding-based search used in RAG systems.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Machine learning models learn patterns from data",
    "Neural networks are inspired by the human brain",
    "Python is a popular programming language for data science",
    "The weather today is sunny and warm",
    "Deep learning uses layers of neurons to process information",
]

query = "How do AI models learn from information?"

vectorizer = TfidfVectorizer()
all_texts = documents + [query]
tfidf_matrix = vectorizer.fit_transform(all_texts)

query_vector = tfidf_matrix[-1]
document_vectors = tfidf_matrix[:-1]

similarities = cosine_similarity(query_vector, document_vectors)[0]

print(f"Query: {query}\n")
print("Documents ranked by relevance:")
ranked_indices = similarities.argsort()[::-1]
for idx in ranked_indices:
    print(f"Score {similarities[idx]:.3f}: {documents[idx]}")
