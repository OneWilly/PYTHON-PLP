def run_quiz():
    """Runs a multiple-choice quiz and displays the score."""

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": "Paris",
        },
        {
            "question": "Which movie won the Oscar for Best Picture in 2020?",
            "options": ["Parasite", "1917", "Joker", "Once Upon a Time in Hollywood"],
            "answer": "Parasite",
        },
        {
            "question": "What is the result of 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4",
        },
        {
            "question": "Which programming language is known for its readability?",
            "options": ["C++", "Java", "Python", "Assembly"],
            "answer": "Python",
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Mars", "Earth", "Jupiter", "Saturn"],
            "answer": "Jupiter",
        },
    ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")

        user_answer = input("Enter your answer (1, 2, 3, or 4): ")
        try:
          user_answer_index = int(user_answer) -1
          if q["options"][user_answer_index] == q["answer"]:
              print("Correct!")
              score += 1
          else:
              print(f"Incorrect. The correct answer is {q['answer']}.")
        except (ValueError, IndexError):
          print("Invalid input. The correct answer is " + q["answer"])

    print(f"\nYour final score is: {score}/{len(questions)}")
    return score, len(questions)

def play_again():
  """Asks the user if they want to play again."""
  while True:
    play = input("Do you want to play again? (yes/no): ").lower()
    if play == "yes":
      return True
    elif play == "no":
      return False
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """Main function to run the quiz and handle play again."""
    while True:
        score, total = run_quiz()
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()