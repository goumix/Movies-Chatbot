from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")


def mistral_response(prompt):
    completion = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "You are a movie expert"},
        {"role": "user", "content": prompt}
    ],
    temperature=0.5,
    )
    return completion
