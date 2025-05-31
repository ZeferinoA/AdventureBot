import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

model = genai.GenerativeModel('gemini-pro')

name = input("What's your name")
print(f"Hello, {name}, Welcome to Adventure bot")
prompt = input("Enter a prompt")

for x in range(0,9,1):
  response = model.generate_content(prompt)
  print(response.text)
  prompt = input(response)

response = model.generate_content(prompt)
print(response.text)
print(f"Thanks for Playing {name}")
