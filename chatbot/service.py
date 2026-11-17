from collections.abc import Sequence

import cohere

MODEL = "command-a-03-2025"


def ask_cohere(api_key: str, messages: Sequence[dict[str, str]]) -> str:
    client = cohere.ClientV2(api_key=api_key)
    response = client.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant.",
            },
            *messages,
        ],
    )

    if not response.message.content or not response.message.content[0].text:
        raise ValueError("Cohere returned an empty response.")

    return response.message.content[0].text
