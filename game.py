import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = #APIkey
model = genai.GenerativeModel('gemini-pro')

name = input("What's your name")
print(f"Hello, {name}, Welcome to Adventure bot")
prompt = input("Enter a prompt")

for x in range(0,9,1):
  response = model.generate_content(prompt)
  print(response.text)
  prompt = input(response)

response = moderl.generate_content(prompt)
print(response.text)
print(f"Thanks for Playing {name}")
