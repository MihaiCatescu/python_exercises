'''
Make a two-player Rock-Paper-Scissors game.

Remember the rules:

- Rock beats scissors
- Scissors beats paper
- Paper beats rock
'''

print("Hello players! Welcome to Rock-Paper-Scissors! Insert your choice in the prompts that will appear bellow. \n"
      "As general rules: \n"
      "Rock beats Scissors\n"
      "Paper beats Rock\n"
      "Scissors beats Paper\n"
      "If any of you want to end the game, simply, enter 'Quit' in the prompt.\n"
      "Have fun!")

choices = ["rock", "paper", "scissors"]

while True:
    player_one = input("Player One, enter your command: ")
    player_two = input("Player Two, enter your command: ")
    player_one = player_one.lower()
    player_two = player_two.lower()
    if player_one == "quit" or player_two == "quit":
        print("Game ended!")
        break
    elif player_one == "rock" and player_two == "scissors":
        print("Rock beats scissors! Player One wins!")
    elif player_two == "rock" and player_one == "scissors":
        print("Rock beats scissors! Player Two wins!")
    elif player_one == "rock" and player_two == "paper":
        print("Paper beats rock! Player One wins!")
    elif player_two == "rock" and player_one == "paper":
        print("Paper beats rock! Player Two wins!")
    elif player_one == "scissors" and player_two == "paper":
        print("Scissors beats paper! Player One wins!")
    elif player_two == "scissors" and player_one == "paper":
        print("Scissors beats paper! Player Two wins!")
    elif player_one == player_two:
        print("It's a draw! Try again!")
    elif player_one != choices or player_two != choices:
        print("You did not select one of the three choices. Try again!")