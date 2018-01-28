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
        return output+'\n'
        
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
        # if very value of 1 row is a 1 or a 2
        # if row1[n], row2[2], and row3[n] are all 1 or 2
        # if row1[n], row2[n+1], row3[n+2]
        # if row1[n], row2[n-1], row3[n-2]
        # if every position is a 1 or 2, but no winner
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
                
def welcome():
    print("                                                ")
    print("\t\   /\    /  __      __              __ ")
    print("\t \ /  \  /  |__ |   |   |||  /\ /\  |__  ")
    print("\t  \    \/   |__ |__ |__ ||| /  \  \ |__  ")
    print("                                                ")
    print("\n\tWelcome to Tic Tac Toe 5000 XTREME!")
  
"""
████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗
   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝
   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝
                                                                        
    """
    
def printWinner(player):
    print("\nPlayer ", player, "wins!! ")
    print('\n')

if __name__ == "__main__":
    welcome()
    boardgame = main()
    
    # test()
    
"""
TODO
ASCII welcome art
Implement computer generated moves so you can play a game
testing

"""