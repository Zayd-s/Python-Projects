import random

def play():
    user = input("Let's play Rock paper scissors, \n'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's']) #computer is randomly picking one from #important random

    if user == computer: # if the user and computer choose the same R/P/S
        return 'It\'s a tie'

    if is_win(user, computer): #if is_win functions is true - if user picks these against computer
        return 'You win!'

    return "You lose!" # no need for else, because none of the if statements are true, so it just ends with this return


def is_win(player, opponent): #function for preparing a win
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

print(play())