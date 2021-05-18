
"""
This is a famous casino game "ROULETTE". Where punter has various option of betting
across the table ranging from individual numbers 1 to 36 which has paying odds of 1:36.
There are 6 different combinations of dozens and halves each, each pays 1:3 and 1:2 respectively.
There is a picture for visual reference.
"""


import random
# from simpleimage import SimpleImage


"""
Constants to keep record of various combinations of betting options. These list can later 
be accessed to check if winning number falls in that list if a bet was made on that particular
betting option. These are constants because these lists doesnt change and remain same.
"""

ALL_DOZENS = [list(range(1, 13, 1)), list(range(13, 25, 1)), list(range(25, 37, 1)), list(range(1, 35, 3)), list(range(2, 36, 3)), list(range(3, 37, 3))]
BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
ALL_HALVES = [list(range(1, 19, 1)), list(range(19, 37, 1)), list(range(2, 37, 2)), list(range(1, 36, 2)), BLACK, RED]


def main():
    player_name = welcome()  # welcome message and returns player name
    total_chips = 200  # by default player gets 200 chips to start with.
    while total_chips > 0:  # game starts and carries on as far as player has chips, though player can choose to quit at end of each round.
        singles, total_chips = single_no_bets(total_chips)  # calls funtion, which returns bets on individual numbers and amount of chips on each number in a list
        dozens, total_chips = dozens_bets(total_chips)  # calls funtion, which returns bets on combi of dozens and amount of chips on each number in a list
        halves, total_chips = halves_bets(total_chips)  # calls funtion, which returns bets on combi of halves and amount of chips on each number in a list
        total_chips = calculate_winnings(singles, dozens, halves, total_chips)  # function is called to calculate the chips won/lost in current round. returns total chips after adding win/loss of current round
        total_chips = continue_or_takehome(total_chips, player_name)  # function is called to give player option to buy-in, carry on or withdraw.


# function takes input from user for bets on individual numbers. It returns a list of index 0 and 1
# if any bets are placed on individual numbers. Also returns remaining total_chips.
def single_no_bets(total_chips):
    numbers_to_bet = input("How many single numbers you want to bet on? ")
    numbers_to_bet = check_valid_response(numbers_to_bet, total_chips)
    print()
    single_bets = [[], []]
    if total_chips > 0:
        for i in range(numbers_to_bet):
            if total_chips == 0:
                break
            number = input("Enter the number you want to bet on between 0 to 36: ")
            while not number.isdigit() or int(number) > 36 or int(number) < 0:
                number = input("Invalid number, Please choose between 0 to 36: ")
            number = int(number)
            chips = input("How many chips you want to bet on that num: ")
            chips = check_valid_response(chips, total_chips)
            total_chips -= chips
            info(total_chips)
            single_bets[0] += [number]
            single_bets[1] += [chips]
    return single_bets, total_chips


# function takes bets on dozen/s by user . It return a list, dozen of length of number of dozens bet on.
def dozens_bets(total_chips):
    dozen_list = ['FIRST DOZEN', 'SECOND DOZEN', ' THIRD DOZEN', 'BOTTOM ROW DOZEN', 'MIDDLE ROW DOZEN', 'TOP ROW DOZEN']
    dozen_bets, total_chips = get_bets(total_chips, dozen_list)  # calls get_bet() function.
    return dozen_bets, total_chips


# function takes halves bets from user for 6 different halfs betting options. It returns a list, halves
# which is of length of the number of half combinations bet on.
def halves_bets(total_chips):
    all_halves = ['FIRST HALF', 'SECOND HALF', 'EVEN NUMBERS', 'ODD NUMBER', 'RED NUMBER', 'BLACK NUMBERS']
    half_bets, total_chips = get_bets(total_chips, all_halves)  # calls get_bet() function.
    return half_bets, total_chips


# Function to get bets from user on various betting options like dozens and halves and returns a list with length
# equalling the number of bets made in that betting option. Also returns total chips remaining.
# It has two parameter, total_chips and a list which contains the 'names' as betting option of that segment
# like dozens and halves segment.
def get_bets(total_chips, list_of_betting_option):
    bets = []
    if total_chips > 0:
        for item in list_of_betting_option:
            if total_chips == 0:
                break
            cal_bet = input("Enter the amount of chips you want to bet on " + item + ": ")
            cal_bet = check_valid_response(cal_bet, total_chips)
            total_chips -= cal_bet
            info(total_chips)
            bets += [cal_bet]
    return bets, total_chips


# calculates winnings on different betting options. Gives round end message giving a tally of wins
# and losses on different options. returns total chips after net win/loss.
def calculate_winnings(singles, dozens, halves, total_chips):
    winner_num = pick_winner_num()
    single_win_chips = calc_single_win(singles, winner_num)
    dozen_win_chips = calc_dozen_win(dozens, winner_num)
    half_win_chips = calc_half_win(halves, winner_num)
    total_chips = round_end_message(total_chips, single_win_chips, dozen_win_chips, half_win_chips)
    return total_chips


# function generates a winner number randomly between 0 and 36 both inclusive. Displays the winniner number to user.
# return the winnning number to calculate the winnings in different functions.
def pick_winner_num():
    num = random.randint(0, 36)
    print("And the winning number is......: ", num)
    return num


# function calculates winning on single number bets if there was a bet on winning number.
# it checks for every element in singles[0] as there is where numbers bet on are stored.
def calc_single_win(singles, winner_num):
    single_win_chips = 0
    for i in range(len(singles[0])):
        if winner_num == singles[0][i]:
            single_win_chips += (singles[1][i] * 36)
    print()
    print("Chips won in single numbers : ", single_win_chips)
    return single_win_chips

# function calculate winnings on dozen that were bet on if winning
# number falls in those dozens by accessing the CONSTANT list/s.
def calc_dozen_win(dozens, winner_num):
    dozen_win_chips = 0
    for i in range(len(dozens)):
        if winner_num in ALL_DOZENS[i]:
            dozen_win_chips += (dozens[i] * 3)
    print()
    print("Chips won in dozens :", dozen_win_chips)
    return dozen_win_chips

# function calculate winnings on halves that were bet on if winning
# number falls in those dozens by accessing the CONSTANT list/s.
def calc_half_win(halves, winner_num):
    half_win_chips = 0
    for i in range(len(halves)):
        if winner_num in ALL_HALVES[i]:
            half_win_chips += (halves[i] * 2)
    print()
    print("Chips won in halves :", half_win_chips)
    return half_win_chips


# calculates the total chips and total chips remaining. prints a round end message as well. returns total chips.
def round_end_message(total_chips, single_win_chips, dozen_win_chips, half_win_chips):
    total_chips_won = single_win_chips + dozen_win_chips + half_win_chips
    total_chips += total_chips_won
    if total_chips_won > 0:
        print()
        print("Winner winner, chicken dinner. You've won", total_chips_won, "chips")
    else:
        print()
        print("You won 0 chips in this round")
    if total_chips > 0:
        print()
        print("Your total chips in hand now: " + str(total_chips) + ".")
    else:
        print()
        print("You have lost all your chips in this round.")
        print()
    return total_chips


# asks the user if wants to continue or withdraw in case if remaining chips are more than 0.
# otherwise program ends itself if remaining chips are zero. returns total chips.
def continue_or_takehome(total_chips, player_name):
    if total_chips > 0:
        player_wish = input("Press 1 to continue or 0 to take home your remaining chips: ")
        while not player_wish.isdigit() or int(player_wish) > 2 or int(player_wish) < 0:
            player_wish = input("Invalid response, Press 1 to continue or 0 to take home your remaining chips: ")
        player_wish = int(player_wish)
        print()
        if player_wish == 0:
            print("It was pleasure having you " + player_name + ". You take " + str(total_chips) + " chips in winnings.")
            total_chips = 0
            print()
            print("---------------------------------------| THANK YOU |------------------------------------------------")
        else:
            print()
            print("Good Luck..")
            print()
            print("Place your bets....")
            print()
    else:
        player_wish = input("Enter 1 to buy-in chips or 0 to quit: ")
        player_wish = check_valid_response(player_wish, 1)
        if player_wish == 1:
            add_chips = input("Enter the amount of chips you want to add upto maximum of 200: ")
            add_chips = check_valid_response(add_chips, 200)
            total_chips += add_chips
            print()
            print("Good Luck..")
            print()
            print("Place your bets....")
            print()
        else:
            print("It was pleasure having you " + player_name + ". You take 0 chips in winnings")
            print()
            print("-----------------------------------------|THANK YOU |-----------------------------------------------")
    return total_chips


def welcome():  # prints welcome message and returns players name.
    # image = SimpleImage('roulette.jpeg')
    # image.show()
    print("--------------------------------------------------------------------------------------")
    print()
    print("Welcome, This is the game of Roulette.")
    print("Attached is a picture for the visual refrence.")
    print()
    print("Betting options are as follows:")
    print()
    print("1. Betting on individual numbers (1 to 36) gives you 1:36 in winnings.")
    print()
    print("2. Dozens gives you 1:3 in winnings. There are total 6 combination of")
    print("   dozens. 1-12, 13-24, 25-36 and bottom row, middle row and top row.")
    print()
    print("3. Halves which gives you 1:2 in winnings. There are")
    print("   6 diffrent kind of halves. 1-18, 19-36, black numbers, red numbers, even numbers and")
    print("   odd numbers. Refer to image in case of doubt before betting.")
    print()
    print("-------------------------------|  GAMBLE RESPONSIBLY  |---------------------------------")
    print()
    print("----------------------------------------------------------------------------------------")
    print()
    name = input("Please enter your name: ")
    print()
    print("Hello,", name, ". Welcome to Roulette. You have 200 chips to try your luck. Good Luck.")
    print()
    print("Place your bets.....")
    print()
    return name


# checks for valid response, if its not a integar and greater than remaining chips, it keeps looping untill
# valid response is received from user. returns input casted in int.
def check_valid_response(input_str, total_chips):
    while not input_str.isdigit() or int(input_str) > total_chips:
        input_str = input("Invalid response, refer information above for valid inputs: ")
    return int(input_str)


def info(total_chips):  # function prints info of remaining chips.
    print("You have", total_chips, "chips remaining.")
    print()


if __name__ == "__main__":
    main()