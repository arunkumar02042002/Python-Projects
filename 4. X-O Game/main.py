class GameBoard:
    def __init__(self) -> None:
        self.game_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def set_items(self, user, position, game_board):
        game_board[position] = user
        return game_board
    
    @property
    def gameBoard(self):
        return self.game_board
        
    def clearboard(self):
        self.game_board = {1: ' ', 2: ' ', 3: ' ', 4: '', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def is_place_taken(self, game_board, position):
        return game_board[position] != " "
    
    def is_board_full(self, game_board):
        for v in game_board.values():
            if v == " ":
                return False
        return True
    
    def is_game_won(self, game_board):
        win_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for condition in win_conditions:
            if game_board[condition[0]] == game_board[condition[1]] and game_board[condition[1]] == game_board[condition[2]] and game_board[condition[0]] != " ":
                return True
        return False
    
    def printBoard(self, game_board):
        for k, v in game_board.items():
            if k%3 == 0:
                print (v)
            else:
                print(v, end = "|")


class Game:
    def game_start(self):
        self.controlBoard = GameBoard()
        self.game_board = self.controlBoard.game_board
        self.playerOne = 'O'
        self.playerTwo = 'X'
        print("Let's Play X-O Game")
        self.playerOneName = input("Enter Player One Name: ")
        self.playerTwoName = input("Enter Player Two Name: ")
        print("This is the sanpshot of the gameboard. Each place is represented using 1 - 9.")
        self.controlBoard.printBoard(self.game_board)
        self.turn = 1

    def game_End(self):
        if self.game_running == False:
            replay = input("Press 0 to quit and 1 to play again: ")
            try:
                if int(replay):
                    self.game_running = True
                    self.game_start()
            except:
                print("Enter a valid number.")
                self.game_End()

    def take_turn(self, user, item):
        try:
            print(f"'{user}' choose a place between 1-9: ", end="")
            position = int(input())
            if position > 9 and position < 1:
                raise Exception
        except Exception as e:
            # print("Pick a number between 1-9: ", end="")
            return self.take_turn(user, item)

        if self.controlBoard.is_place_taken(self.game_board, position):
            print("That place is already taken.")
            self.take_turn(user, item)
        
        else:
            self.controlBoard.set_items(item, position, self.game_board)
            self.controlBoard.printBoard(self.game_board)
            if self.controlBoard.is_game_won(self.game_board):
                print(f"{user} wins")
                self.game_running = False

    def main(self):
        self.game_running = True
        self.game_start()
        while self.game_running:
            if self.turn%2 != 0:
                self.take_turn(self.playerOne, 'O')
            else:
                self.take_turn(self.playerTwo, 'X')

            if self.controlBoard.is_board_full(self.game_board):
                print("Its a draw!")
                self.game_running=False
            
            self.turn += 1
        
        if not self.game_running:
            self.game_End()


if __name__ == "__main__":
    Game().main()