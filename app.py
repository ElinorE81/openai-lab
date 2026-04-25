from flask import Flask
import os
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def hello():
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "<h1>Error: OpenAI API Key is missing!</h1>"

    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Tell me a short joke about Kubernetes or DevOps."}],
            temperature=0.7
        )
        joke = response.choices[0].message.content
        return f"<h1>Welcome to Elinor's DevSecOps App! 🚀</h1><p>Here is an AI joke for you:</p><h3><i>{joke}</i></h3>"
    except Exception as e:
        return f"<h1>Error communicating with OpenAI:</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
