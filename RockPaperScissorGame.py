import random

def determine(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
      
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice == 'exit':
            print("Thanks for playing! Final scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

       
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        
        result = determine(user_choice, computer_choice)

       
        print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
        print(result)

       
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        
        print(f"Current scores: You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Type 'exit' to end the game at any time.")
    play_game()
