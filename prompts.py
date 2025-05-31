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