import copy

ALL_SPACES = list("123456789") #the keys for tic tac toe board
X, O, BLANK = "X", "O", " " #constants for string values

class TicTacToeBoard:
    def __init__(self):
        """"Create a new blank tic tac toe board"""
        self._spaces = {}
        for space in ALL_SPACES:
            self._spaces[space] = BLANK
    
    def get_board(self):
        """Return a text representation of the board"""

        result = f"""
        {self._spaces["7"]}|{self._spaces["8"]}|{self._spaces["9"]}     7 8 9
        -+-+-
        {self._spaces["4"]}|{self._spaces["5"]}|{self._spaces["6"]}     4 5 6
        -+-+-
        {self._spaces["1"]}|{self._spaces["2"]}|{self._spaces["3"]}     1 2 3
        """
        return result

    def is_valid_space(self, space: str) -> bool:
        """Returns True if the space on the board is a valid space number and the space is blank"""

        result =  (space in ALL_SPACES) and (self._spaces[space] == BLANK)
        return result
    
    def is_winner(self, player: str) -> bool:
        s, p = self._spaces, player # Shorter names as "syntactic sugar"

        result = (
            (s["1"] == s["2"] == s["3"] == p) or
            (s["4"] == s["5"] == s["6"] == p) or
            (s["7"] == s["8"] == s["9"] == p) or
            (s["1"] == s["4"] == s["7"] == p) or
            (s["2"] == s["5"] == s["8"] == p) or
            (s["3"] == s["6"] == s["9"] == p) or
            (s["1"] == s["5"] == s["9"] == p) or
            (s["3"] == s["5"] == s["7"] == p) 
        )
        return result
    
    def is_board_full(self):
        """Return True if every space on the board has been taken"""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False
        return True

    def update_board(self, space: str, player: str):
        """Sets the space on the board to player"""
        self._spaces[space] = player

class HintBoard(TicTacToeBoard):
    def get_board(self) -> str:
        """Return a text-representation of the board with hints"""
        board = super().get_board()  # Call get_board() from TTTBoard

        x_can_win = False
        o_can_win = False
        original_spaces = self._spaces  # Backup _spaces
        
        for space in ALL_SPACES:
            # Simulate X moving on this space:
            self._spaces = copy.copy(original_spaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.is_winner(X):
                x_can_win = True
            # Simulate O moving on this space
            self._spaces = copy.copy(original_spaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.is_winner(O):
                o_can_win = True
        if x_can_win:
            board = board + "\nX can win in one more move."
        if o_can_win:
            board = board + "\n0 can win in one more move."
        self._spaces = original_spaces
        return board


def main():
    """Runs a game of tic-tac-toe"""

    print("Welcome to tic-tac-toe!")
    game_board = HintBoard()
    current_player, next_player = X, O
    
    while True:
        print(game_board.get_board())  # Display the board on the screen
        
        # Keep asking the player until they enter a number 1-9:
        move = None
        while not game_board.is_valid_space(move):
            print(f"What is {current_player}'s move? (1-9)")
            move = input()
        game_board.update_board(move, current_player)
        
        if game_board.is_winner(current_player):  # Check if the game is over
            print(game_board.get_board())
            print(f"{current_player} has won the game!")
            break
        elif game_board.is_board_full():  # Next check for a tie
            print(game_board.get_board())
            print("The game is a tie!")
            break
        current_player, next_player = next_player, current_player  # Swap turns
    print("Thanks for playing!")

if __name__ == "__main__":
    main()