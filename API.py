from google import genai
import os

client = genai.Client(api_key=os.getenv("YOUR API KEY"))

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="You are Jarvis, a helpful AI assistant. Reply naturally to the user."
)

print(response.text)
