"""
Professionalization pass: automated test for Lesson 28's LLM helper
functions, using mocking to avoid real API calls in tests.

Demonstrates a core professional testing pattern: code that calls
external services (APIs, LLMs) should be tested with the real call
mocked out - this makes tests fast, free, deterministic, and
independent of network/API availability.
"""

from unittest.mock import MagicMock, patch
from lesson28_llm_basics import approximate_token_count, ask_llm


def test_approximate_token_count():
    assert approximate_token_count("hello world") == 2
    assert approximate_token_count("one two three four") == 4
    assert approximate_token_count("") == 0


@patch("lesson28_llm_basics.client")
def test_ask_llm_returns_mocked_response(mock_client):
    """Verify ask_llm correctly extracts content from the API response,
    without making a real network call."""
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "This is a mocked answer"
    mock_client.chat.completions.create.return_value = mock_response

    result = ask_llm("Any prompt")

    assert result == "This is a mocked answer"
    mock_client.chat.completions.create.assert_called_once()
