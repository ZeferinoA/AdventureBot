# LLM utilities and calls.

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import build_prompt

# Now we just need to load the API key
load_dotenv() # Load the information from the key location
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # Search our files for the variable set to GOOGlE_API_KEY

# Setting up the model baby
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_story(base_prompt, history):
    """
    This is the api function call to generate the story!
    
    base_prompt: The story prompt that the user first passes in
    history: The previous story choices and what happened (for context)
    """

    prompt = build_prompt(base_prompt, history)

    try:
        response = model.generate_content(prompt)
        response_text = response.text

        if response_text.startswith('```json'):
            response_text = response_text.replace('```json', '').replace('```', '').strip()
        elif response_text.startswith('```'):
            response_text = response_text.replace('```', '').strip()


        story_data = json.loads(response_text)
        return story_data["story"], story_data["options"]
    
    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")
        print(f"Raw response was: {response_text}")
        return "The AI didn't respond in the right format!", ["Try again", "Exit"]
    
    except Exception as e:
        print("Error calling Gemini:", e)
        return "Something went wrong with the story!", ["Try again", "Exit"]
    
