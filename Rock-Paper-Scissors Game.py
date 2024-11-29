import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter 'rock', 'paper', or 'scissors'. Type 'exit' to quit.")

    while True:
        player_choice = input("Your choice: ").lower()
        if player_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)
        if winner == "draw":
            print("It's a draw!")
        elif winner == "player":
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    main()
