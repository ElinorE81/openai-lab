from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a DIFFERENT joke about programmers. Don't mention light or bugs."} 
    ],

    store=False, 
    temperature=0.7
)

print(response.choices[0].message.content)
