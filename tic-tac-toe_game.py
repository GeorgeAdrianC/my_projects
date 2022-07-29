""" Welcome to my tic-tac-toe game"""


def is_winner(numpad, char):
    if numpad[1] == char and numpad[2] == char and numpad[3] == char:
        return True
        
    elif numpad[4] == char and numpad[5] == char and numpad[6] == char:
        return True
        
    elif numpad[7] == char and numpad[8] == char and numpad[9] == char:
        return True
        
    elif numpad[7] == char and numpad[4] == char and numpad[1] == char:
        return True
        
    elif numpad[8] == char and numpad[5] == char and numpad[2] == char:
        return True
        
    elif numpad[9] == char and numpad[6] == char and numpad[3] == char:
        return True
        
    elif numpad[1] == char and numpad[5] == char and numpad[9] == char:
        return True
        
    elif numpad[7] == char and numpad[5] == char and numpad[3] == char:
        return True
    return False        


def main():
    while True:
        numpad = [" "," "," "," "," "," "," "," "," "," "]

        while True:
            start_or_stop = input("Do you want to play? Type 'Yes' or 'No: ")
            if start_or_stop == "No" or start_or_stop =="no":
                print("Have a good day!")
                exit()
            elif start_or_stop == "Yes" or start_or_stop == "yes":
                break
            else:
                print("Please type 'Yes' or 'No'.")
                
        while True:
            chose_XO = input("Hello! Choose between 'X' or 'O':")
            if chose_XO == "x" or chose_XO == "X":
                first_choice = "X"
                break
            elif chose_XO == "o" or chose_XO == "O":
                first_choice = "O"
                break
            else:
                print("Please choose between 'X' or 'O'.")

        second_choice = " "
        if first_choice == "X":
            second_choice = "O"
        elif first_choice == "O":
            second_choice = "X"
        else:
            pass

        while True:
            move1 = int(input(f"'{first_choice}' choose your position (1-9): "))
            numpad[move1] = first_choice
            move2 = int(input(f"'{second_choice}' choose your position (1-9): "))
            numpad[move2] = second_choice
            board = f"{numpad[7]} | {numpad[8]} | {numpad[9]} \n__________\n{numpad[4]} | {numpad[5]} | {numpad[6]} \n__________\n{numpad[1]} | {numpad[2]} | {numpad[3]}"
            print(board)
            if is_winner(numpad, "X"):
                print("X is winner!\n Game over!")
                break
            if is_winner(numpad, "O"):
                print("O is winner!\n Game over!")
                break

        print("\nThank you for playing!")
        
        while True:
            replay = input("Do you want to play again? Enter Yes or No: ")
            if replay == "No" or replay == "NO" or replay == "no":
                exit()
            elif replay == "Yes" or replay == "yes" or replay == "YES":
                break
            else:
                print("Please type Yes or No.")

if __name__ == "__main__":
    main()