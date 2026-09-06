"""
Lesson 32: AI Agents & Tool Calling

Demonstrates the core agent architecture: describing tools to an LLM,
letting the model decide whether and which tool to call, executing
that tool for real, and feeding the result back for a final answer.
This is the same mechanism behind Claude's tool use and modern AI
agent frameworks.
"""

import json
import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_weather(city: str) -> str:
    """A fake weather tool - a real one would call a weather API."""
    fake_weather = {
        "mogadishu": "32°C, sunny",
        "london": "14°C, rainy",
        "tokyo": "22°C, cloudy",
    }
    return fake_weather.get(city.lower(), "Weather data not available for that city")


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "The city name"}
                },
                "required": ["city"],
            },
        },
    }
]


def run_agent(user_question: str) -> str:
    """Full agent loop: ask the LLM, execute any tool it requests, get final answer."""
    messages = [{"role": "user", "content": user_question}]

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools,
        max_tokens=300,
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if not tool_calls:
        return response_message.content

    messages.append(response_message)

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        if function_name == "get_weather":
            result = get_weather(function_args.get("city"))
        else:
            result = "Unknown tool"

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        })

    final_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        max_tokens=300,
    )

    return final_response.choices[0].message.content


if __name__ == "__main__":
    question = "What's the weather like in Mogadishu right now?"
    print(f"Question: {question}\n")
    answer = run_agent(question)
    print(f"Agent's answer: {answer}")
