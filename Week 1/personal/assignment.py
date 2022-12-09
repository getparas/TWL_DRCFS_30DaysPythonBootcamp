import random

options = ("rock","paper","scissors")
playing = True

while playing:
    player = None

    computer = random.choice(options);
    while player not in options:
        player = input("Enter a choice (rock,paper,scissors): ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissprs":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    # playAgain = input("Play again? (y/n): ").lower()
    # if not playAgain =="y":
    #     playing = False
    if not input("Play again? (y/n): ").lower() == "y":
        playing = False
print("Thanks for playing!")
        