import random


# file i/o function for historical results
def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history


def save_results(w, t, l):
    text_file = open('history.txt', 'w')
    text_file.write(w + "," + t + "," + l)
    text_file.close()


# welcome message
results = load_results()
wins = 0  # int(results[0])
ties = 0  # int(results[1])
losses = 0  # int(results[2])
print("Welcome to Rock, Paper, Scissors!")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue....")

# initialize user, computer choices
computer = random.randint(1, 3)
user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))

# gameplay loop
while not user == 9:
    # user chooses ROCK
    if user == 1:
        if computer == 1:
            print("Computer chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper...Computer wins!")
            losses += 1
        elif computer == 3:
            print("Computer chose scissors...you win!")
            wins += 1

    # user chooses PAPER
    elif user == 2:
        if computer == 1:
            print("Computer chose rock...you win!")
            wins += 1
        elif computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        elif computer == 3:
            print("Computer chose scissors...Computer wins!")
            losses += 1

    # user chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("Computer chose rock...Computer wins!")
            losses += 1
        elif computer == 2:
            print("Computer chose paper...you win!")
            wins += 1
        elif computer == 3:
            print("Computer chose scissors...tie!")
            ties += 1

    # user enters an invalid choice
    print("Invalid selection. Please try again...")

    # print updated stats
    print(f'Wins: {wins}, Ties: {ties}, Losses: {losses}')

    # prompt user to make another selection
    print("Please choose to continue...")
    computer = random.randint(1, 3)
    user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))

# game over, save results
# save_results(wins, ties, losses)
