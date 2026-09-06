"""
Lesson 28: LLM Basics - Tokens, Prompts & API Calls

Demonstrates the fundamental mechanics behind Generative AI: how text
becomes tokens, how a prompt is sent to a Large Language Model, and
how the model's response is retrieved and used - directly connecting
to the architecture behind Claude, GPT, and the user's own Termux AI
project.
"""

import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def approximate_token_count(text: str) -> int:
    """
    Rough estimate of token count. Real tokenizers (like GPT's tiktoken)
    split on subwords, not just spaces - this is a simplified approximation
    for teaching purposes, not the real algorithm.
    """
    return len(text.split())


def ask_llm(prompt: str) -> str:
    """Send a prompt to the LLM and return its text response."""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
    )
    return response.choices[0].message.content


prompt = "In one sentence, explain what a neural network is."

print(f"Prompt: {prompt}")
print(f"Approximate token count of prompt: {approximate_token_count(prompt)}")

print("\nSending to LLM...")
answer = ask_llm(prompt)

print(f"\nLLM response: {answer}")
print(f"Approximate token count of response: {approximate_token_count(answer)}")
