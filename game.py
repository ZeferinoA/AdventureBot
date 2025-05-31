from llm_utils import generate_story
from colorama import Fore, Style, init
import pyttsx3
init(autoreset=True)
engine = pyttsx3.init()
engine.setProperty('rate', 200)

def main():
  name = input("What's your name ")
  print(f"{Fore.CYAN} Hello, {name}, Welcome to Adventure bot")

  base_prompt = input("Enter your story idea: ")
  history = []

  print("\n" + "="*50)
  print(f"{Fore.CYAN} Starting your adventure...")
  print("\n" + "="*50)

  for turn in range(1, 10):
    print(f"--- Turn {turn} ---")

    story_text, options = generate_story(base_prompt, history)

    print(f"\n{story_text}\n")
    engine.say(story_text)
    engine.runAndWait()

    print(f"{Fore.CYAN} What do you choose")
    for option in options:
      print(f"{option}")
      engine.say(option)
      engine.runAndWait()
    
    while True:
      try:
        choice = int(input("\nEnter your choice (1 or 2): "))
        if choice in [1, 2]:
          chosen_option = options[choice - 1]
          break
        else:
          print(f"{Fore.YELLOW} Please enter 1 or 2.")
      except ValueError:
        print(f"{Fore.RED} Please enter a valid number (1 or 2).")

    history.append(f"Story: {story_text}")
    history.append(f"Player chose: {chosen_option}")

    print(f"\nYou chose: {chosen_option}")
    engine.say(chosen_option)
    engine.runAndWait()
    print("-" * 30)

  print(f"\n--- Final Turn ---")
  final_story, _ = generate_story(base_prompt, history + ["This is the final part of the adventure. Provide an epic conclusion."])
  print(f"\n{final_story}\n")
  engine.say(final_story)
  engine.runAndWait()

  print("="*50)
  print(f"{Fore.GREEN} Thanks for playing, {name}! Your adventure has ended.")
  print("="*50)

if __name__ == "__main__":
  main()
