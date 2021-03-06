class Board():
    def __init__(self, board=None):
        if not board:
            self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        else:
            assert type(board) is list
            if len(board) != 3 or len(board[0])!=3:
                raise Exception("Incorrect Board Input: Must be a 3x3 array")
            else:
                self.board = board
        self.game_over = False
        
    def __repr__(self):
        output = ''
        for row in self.board:
            output += "\n\t"
            for r in row:
                output+=str(r)
                output += ' '
        return output+'\n\n'
        
    def setValue(self, indices, val):
        if self.isLegal(indices, val):
            self.board[indices[0]][indices[1]] = val
            return True
        return False
        
    def isLegal(self, indices, val):
        try:
            if self.board[indices[0]][indices[1]]!=0:
                print("That space is already occupied.. ")
                return False
            place = self.board[indices[0]][indices[1]]
            return True
        except IndexError:
            raise Exception("value you chose exceed the board dimensions")
        return False
        
    def gameOver(self):
        winner = 0
        winning_combos= [[[0, 0], [1,1], [2,2]], [[0,2],[1,1], [2,0]]]
        for n in range(3):
            winning_combos.append([[n, 0], [n, 1], [n, 2]])
            winning_combos.append([[0,n], [1,n], [2,n]])
        for win_combo in winning_combos:
            [p1x, p1y], [p2x, p2y], [p3x, p3y] = win_combo
            if self.board[p1x][p1y]==self.board[p2x][p2y] and self.board[p2x][p2y] == self.board[p3x][p3y]:
                winner = self.board[p1x][p1y]
                break
        return winner
    
    def playerMove(self, player):
        print("Player: ", player)
        player_input = input("Choose your move by typing two numbers (row and column separate by a space) ")

        try:
            player_input = player_input.strip()
            assert len(player_input) >= 3
            r, c = player_input.split(' ')
            r, c = int(r), int(c)
        except:
            print("Error, invalid input")
        move = self.setValue([r,c], player)
        if move: # player made a successful move
            return
        else:
            print("Choose a different move ")
            self.playerMove(player)
    
class Player():
    def __init__(self, name):
        # screen name
        self.name = name
        self.token = name[0]
        
    def setToken(self, token):
        # define what to place on the board
        self.token = token
                
def welcome():
    print(colors("RESET"))
    print(colors("CYAN"))
    print("                                                ")
    print("  _______ _        _______           _______")
    print(" |__   __(_)      |__   __|         |__   __|")
    print("    | |   _  ___     | | __ _  ___     | | ___   ___")
    print("    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ | ")
    print("    | |  | | (__     | | (_| | (__     | | (_) |  __|")
    print("    |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|")
    print(colors("RED"))
    five_thousand = """
   ____ _  _ ___ ____ ____ _  _ ____
   |___  \/   |  |__/ |___ |\/| |___ ||
   |___ _/\_  |  |  \ |___ |  | |___ ||
                                     oo
    """
    print(five_thousand)
    print(colors("RESET"))

def printWinner(player):
    print("\nPlayer ", player, "wins!! ")
    print('\n')

def colors(colorname):
    color_vals = {"RED":"\033[1;31m",
    "BLUE":"\033[1;34m",
    "CYAN":"\033[1;36m",
    "GREEN":"\033[0;32m",
    "RESET":"\033[0;0m",
    "BOLD":"\033[;1m",
    "REVERSE":"\033[;7m"}
    return color_vals[colorname]

def main():
    boardgame = Board()
    players = [1, 2]
    current_player = 1
    while not boardgame.game_over:
        for player in players:
            print(boardgame)
            boardgame.playerMove(player)
            over = boardgame.gameOver()
            if over:
                printWinner(player)
                boardgame.game_over = True
                return boardgame

if __name__ == "__main__":
    welcome()
    boardgame = main()
    
    # test()
    
"""
TODO
Invalid input moves shouldn't crash the game
    Error handling
Implement computer generated moves so you can play 1 player
Testing and unit tests

"""