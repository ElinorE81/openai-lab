from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a short, funny joke about programmers."} 
    ],

    store=False, 
    temperature=0.7
)

print(response.choices[0].message.content)
