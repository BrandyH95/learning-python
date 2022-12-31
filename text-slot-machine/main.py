#Text Slot Machine
#Author: Brandy Brewer
#Date: 12/31/2022
#Based on YouTube tutorial: https://www.youtube.com/watch?v=th4OBktqK1I&ab_channel=TechWithTim

import random

#GLOBALS
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLUMNS = 3

#symbol dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#value dictionary
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#check if any lines have the same symbols in a row
def check_winnings(columns, lines, bet, values):
    #set winnings to 0
    winnings = 0

    #winning lines list
    winning_lines = []

    #looping through to check each row
    for line in range(lines):
        #sets the symbol we want to check to the symbol in the first column of the current row 
        symbol  = columns[0][line]

        #check each column for the symbol we need to match
        for column in columns:
            #symbol to check is equal to the column at the current row that we are looking at
            symbol_to_check = column[line]

            #if the whole row of symbols match
            if symbol != symbol_to_check:
                #winnings is 0 if symbols don't match, and stops checking the row
                break

        else:
            #winnings is the value of the matching symbols multiplied by the bet the user made
            winnings += values[symbol] * bet
            #numerical value of winning lines added to list 
            winning_lines.append(line + 1)

    return winnings, winning_lines


#generate slot machine outcome
def get_slot_machine_spin(rows, columns, symbols):
    #symbol list
    all_symbols = []

    #adding all the symbols to the symbols list using .items to grab both the key (symbol) and the value (symbol_count) 
    #from the symbol dictionary instead of just the key and manually referencing the value later
    for symbol, symbol_count in symbols.items():
        #using _ instead of i since we don't care about the position/iteration value of the items in the list, avoiding an unused variable later
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #defining columns list
    cols = []

    #generate a column for each column we need, in this case 3
    for _ in range(columns):
        #start with empty column list
        column = []

        #make copy of all symbols list so we don't overwrite it when we remove items that have been chosen already
        current_symbols = all_symbols[:]

        #loop through the number of values we need to put in a column, which is equal to the number of rows we have on the slot machine, so 3 for this
        for _ in range(rows):
            #randomly pick a value from copied list
            value = random.choice(current_symbols)
            #remove chosen value from current symbol list
            current_symbols.remove(value)
            #add new value to column list
            column.append(value)

        #add newly generated column to the cols list
        cols.append(column)

    return cols

def print_slot_machine(cols):
    #Transposing - taking our "horizontal" lists of columns to print them out "vertically" for the game

    #looping through every row we have i.e. number of columns in the columns list
    for row in range(len(cols[0])):
        #for every row we're looping through the items in each of the columns
        #enumerate gives you the index as well as the item at that index
        for i, column in enumerate(cols):
            #print the item in the column that is in the iteration value we're currently at until we reach the end of the list (len - 1 for max index value)
            if i != len(cols) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

#gets deposit from the user
def deposit():
    #set valid deposit flag
    deposit_is_valid = False

    #while no deposit has been made...
    while deposit_is_valid != True:
        #ask user how much they'd like to deposit
        amount = input("What would you like to deposit? $")

        #if amount is not a number, asks for a number
        if not amount.isdigit():
            print("Please enter a valid number for your deposit.")
        
        #if amount is a number it sets it to be an integer
        else:
            amount = int(amount)

            #if amount is less than 0 ask for a number greater than 0
            if amount <= 0:
                print("Amount deposited must be greater than 0.")

            #if the amount is greater than 0, set valid deposit flag to True
            else:
                deposit_is_valid = True

    return amount

#gets number of lines user wants to bet on
def get_lines():
    #set valid lines flag
    lines_is_valid = False

    #while user has not entered the number of lines to play...
    while lines_is_valid != True:
        #ask user how many lines to play
        lines = input("Enter the number of lines you'd like to bet on (1-" + str(MAX_LINES) + "): ")

        #if lines is not a number, asks for a number
        if not lines.isdigit():
            print("Please enter a valid response for the number of lines.")
        
        #if lines is a number it sets it to be an integer
        else:
            lines = int(lines)

            #if lines is between 1 and the max number of lines, flag is True
            if 1 <= lines <= MAX_LINES:
                lines_is_valid = True

            #if the lines is anything else, tells player to pick something in the range
            else:
                print("Number of lines to play must be between 1 and " + str(MAX_LINES) + ".")

    return lines

#get amount the user would like to bet
def get_bet():
    #set valid bet flag
    bet_is_valid = False

    #while no bet has been made...
    while bet_is_valid != True:
        #ask user how much they'd like to deposit
        bet = input("What would you like to bet on each line? $")

        #if bet is not a number, asks for a number
        if not bet.isdigit():
            print("Please enter a valid number for your bet.")
        
        #if bet is a number it sets it to be an integer
        else:
            bet = int(bet)

            #if bet is between min and the max, flag is True
            if MIN_BET <= bet <= MAX_BET:
                bet_is_valid = True

            #if the bet is anything else, tells player to pick something in the range
            else:
                print("Your bet must be between $" + str(MIN_BET) + " and $" + str(MAX_BET) + ".")

    return bet

#single iteration of the game
def spin(balance):
    lines = get_lines()

    #check if bet is less than total balance
    bet_flag = False
    while bet_flag != True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough to bet that amount. Your current balance is: $"+ str(balance) +"")
        else:
            bet_flag = True
    
    print("You are betting $"+ str(bet) +" on "+ str(lines) +" lines. Total bet is equal to: $"+ str(total_bet) +"")

    #passing values to the generator to print the slots
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)

    #checking the slots for any winnings and printing them out
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print("You won $"+ str(winnings) +"!")
    print("You won on lines: ", *winning_lines)

    return winnings - total_bet


#########################
#     Main Function     #
#########################

def main():

    balance = deposit()
    #run game until balance is 0
    while True:
        print("Current balance is $"+ str(balance) +"")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)

    print("You left with $"+ str(balance) +".")

main()

