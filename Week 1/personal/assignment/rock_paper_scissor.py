# rock, paper, scissor game using python
import random

ROCK = 'rock'
PAPER = 'paper'
SCISSOR = 'scissors'
options = (ROCK,PAPER,SCISSOR)
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
    elif player == ROCK and computer == SCISSOR:
        print("You win!")
    elif player == PAPER and computer == ROCK:
        print("You win!")
    elif player == SCISSOR and computer == PAPER:
        print("You win!")
    else:
        print("You lose!")
    # playAgain = input("Play again? (y/n): ").lower()
    # if not playAgain =="y":
    #     playing = False
    # -> shortcut method
    if not input("Play again? (y/n): ").lower() == "y":
        playing = False
print("Thanks for playing!")
        