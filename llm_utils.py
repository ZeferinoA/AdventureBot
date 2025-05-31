# LLM utilities and calls.

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Now we just need to load the API key
load_dotenv() # Load the information from the key location
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # Search our files for the variable set to GOOGlE_API_KEY

# Setting up the model baby
model = genai.GenerativeModel("gemini-pro") # Tell what model we want

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

        import json
        story_data = json.loads(response_text)
        return story_data["story"], story_data["options"]
    
    except Exception as e:
        print("Error calling Gemini:", e)
        return "Something went wrong with the story!", ["Try again", "Exit"]
    
# THIS IS JUST A TEMP FUNCTION TO VERIFY FUNCTIONALITY IT WILL BE TIED INTO GAME.PY LATER
def build_prompt(base_prompt, history):
    return f"""
You are an AI story generator for a choose-your-own-adventure game.

The player's story idea is:
"{base_prompt}"

Here is what has happened so far:
{history}

Continue the story with the next part and give exactly two numbered options to choose from.

Respond **only** in the following JSON format:
{{
  "story": "<next part of the story>",
  "options": ["<Option 1>", "<Option 2>"]
}}
"""