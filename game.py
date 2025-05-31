from llm_utils import generate_story

def main():
  name = input("What's your name")
  print(f"Hello, {name}, Welcome to Adventure bot")

  base_prompt = input("Enter your story idea: ")
  history = []

  print("\n" + "="*50)
  print("Starting your adventure...")
  print("\n" + "="*50)

  for turn in range(1, 10):
    print(f"--- Turn {turn} ---")

    story_text, options = generate_story(base_prompt, history)

    print(f"\n{story_text}\n")

    print("What do you choose")
    for i, option in enumerate(options, 1):
      print(f"{i}. {option}")
    
    while True:
      try:
        choice = int(input("\nEnter your choice (1 or 2): "))
        if choice in [1, 2]:
          chosen_option = options[choice - 1]
          break
        else:
          print("Please enter 1 or 2.")
      except ValueError:
        print("Please enter a valid number (1 or 2).")

    history.append(f"Story: {story_text}")
    history.append(f"Player chose: {chosen_option}")

    print(f"\nYou chose: {chosen_option}")
    print("-" * 30)

  print(f"\n--- Final Turn ---")
  final_story, _ = generate_story(base_prompt, history + {"This is the final part of the adventure. Provide an epic conclusion."})
  print(f"\n{final_story}\n")

  print("="*50)
  print(f"Thanks for playing, {name}! Your adventure has ended.")
  print("="*50)

if __name__ == "__main__":
  main()