from openai import OpenAI

# יצירת חיבור ל-API. 
# הספריה מחפשת אוטומטית את משתנה הסביבה OPENAI_API_KEY
client = OpenAI()

# שליחת הבקשה למודל
response = client.chat.completions.create(
    model="gpt-4o",  # אפשר גם לשנות ל-"gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a short, funny joke about programmers."} # כאן שיניתי את השאלה
    ],
    # הגדרות נוספות
    store=False, 
    temperature=0.7
)

# הדפסת התשובה שחזרה מהמודל
print(response.choices[0].message.content)
