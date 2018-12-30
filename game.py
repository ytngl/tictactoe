class TicTacToe:

    def play(self):
        play = 'y'
        print("Welcome to TicTacToe\n")
        while play == 'y' or play == 'Y':
            board = Board()
            choice = input(("Would you like to be X or O?\n"))
            if choice == 'X' or choice == 'x':
                firstPlayer = Player('X', True)
                secondPlayer = Player('O', False)
            elif choice == 'O' or choice == 'o':
                firstPlayer = Player('O', True)
                secondPlayer = Player('X', False)
            else:
                raise Exception("Invalid Input\n")
            while not board.isFull() and not board.isWon():
                board.printBoard()
                board.printList()
                symbol = ''
                if firstPlayer.turn:
                    positionSelected = int(input("PLAYER X TURN, choose between (1-9): \n"))
                    symbol = firstPlayer.symbol
                else:
                    positionSelected = int(input("PLAYER O TURN, choose between (1-9): \n"))
                    symbol = secondPlayer.symbol
                positionSelected = positionSelected - 1
                if (positionSelected >= 1 or positionSelected <= 9) and board.positionIsEmpty(positionSelected):
                    board.addToBoard(positionSelected, symbol)
                    if firstPlayer.turn: 
                        secondPlayer.turn = True  
                        firstPlayer.turn = False
                    else:
                        secondPlayer.turn = False
                        firstPlayer.turn = True
                else:
                    print("Invalid location\n")
            if board.isFull():
                print("\n-------------")
                print("It's a tie.")
                print("-------------")
                board.printBoard()
            else:
                print("\n-------------")
                print("Player " + str(board.whoWon()) + " won.")
                print("------------")
                board.printBoard()
            play = input("Do you want to play again? y/n\n")
        print("Goodbye!\n")
        return

class Board:
    def __init__(self):
        self.board = list(range(1,10))
        self.playerWon = None

    def printList(self):
        print(self.board)

    def positionIsEmpty(self, position):
        if self.board[position] is not 'X' or self.board[position] is not 'O':
            return True
        else:
            return False

    def addToBoard(self, position, playerSymbol):
        self.board[position] = ''
        self.board[position] = playerSymbol

    def isFull(self):
        for item in self.board:
            if item is not 'O' and item is not 'X':
                return False
        return True

    def isWon(self):
        if (self.board[0] == self.board[1] == self.board[2]):
            self.playerWon = self.board[0]
            return True
        elif (self.board[3] == self.board[4] == self.board[5]):
            self.playerWon = self.board[3]
            return True
        elif (self.board[6] == self.board[7] == self.board[8]):
            self.playerWon = self.board[6]
            return True
        elif (self.board[0] == self.board[3] == self.board[6]):
            self.playerWon = self.board[0]
            return True
        elif (self.board[0] == self.board[4] == self.board[8]):
            self.playerWon = self.board[0]
            return True
        elif (self.board[1] == self.board[4] == self.board[7]):
            self.playerWon = self.board[1]
            return True
        elif (self.board[2] == self.board[5] == self.board[8]):
            self.playerWon = self.board[2]
            return True
        elif (self.board[2] == self.board[4] == self.board[6]):
            self.playerWon = self.board[2]
            return True
        else:
            return False

    def whoWon(self):
        return self.playerWon

    def printBoard(self):
        print(" ")
        print("  " + str(self.board[6]) + " " + "|" + " "  + str(self.board[7]) + " " + "|" + " " + str(self.board[8]))
        print("-------------")
        print("  " + str(self.board[3]) + " " + "|" + " "  + str(self.board[4]) + " " + "|" + " " + str(self.board[5]))
        print("-------------")
        print("  " + str(self.board[0]) + " " + "|" + " "  + str(self.board[1]) + " " + "|" + " " + str(self.board[2]))
        print(" ")

class Player:
    def __init__(self, symbol, turn):
        self.symbol = symbol
        self.turn = turn

def main():
    game = TicTacToe()
    game.play()

main()
