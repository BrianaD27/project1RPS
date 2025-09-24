import random 

def menu_screen():
    global answer

    print("===================================")
    print("Welcome to Rock Paper Scissors!")
    print(" ")
    answer = input("Are you ready to start? (Y/N)? ")

def start_up_message():
    print("Okay lets start!")
    print("Rock")
    print("Paper")
    print("Scissors")
    print("Shoot!")

def selection_process(choice):
    if choice == "1":
        return "Rock"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissors"
    else:
        player_choice = input("Enter Your Selection (1 = Rock, 2 = Paper, 3 = Scissors): ")
        selection_process(player_choice)

def round_check(player_choice, computer):
    if player_choice == computer:
        print("It's a Tie!")
    elif (player_choice == "Rock" and computer == "Scissors") or (player_choice == "Paper" and computer == "Rock") or (player_choice == "Scissors" and computer == "Paper"):
        print("Congrats! You've won!")
    else:
        print("Aww, you lost. Better luck next time!")
        
def game():
    options = ["Rock", "Paper", "Scissors"]
    start_up_message()

    player_choice = input("Enter Your Selection (1 = Rock, 2 = Paper, 3 = Scissors): ")
    player_choice = selection_process(player_choice)

    computer = random.choice(options)

    print(f"You chose: {player_choice}")
    print(f"The Computer chose: {computer}")

    round_check(player_choice, computer)

start = True
while start:
    menu_screen()
    game()
    
    start = input("Would you like to play again? (Y/N): ")
    if start == "Y":
        start = True
    else:
        start = False