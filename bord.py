class Bord:


    player1 = "O"
    player2 = "X"
    turnplayer = player1

    #this will set bord to empty space after game for another game
    def setBord(self):
        print("Game is started")
        self.currentBord = [" " for i in range(9)]

    # TO ONLY DRAW BORD
    def drawBord(self):
        print("|{}|{}|{}|".format(self.currentBord[0], self.currentBord[1], self.currentBord[2]))
        print("|{}|{}|{}|".format(self.currentBord[3], self.currentBord[4], self.currentBord[5]))
        print("|{}|{}|{}|".format(self.currentBord[6], self.currentBord[7], self.currentBord[8]))

    def changeTurn(self):
        if(self.turnplayer == self.player1):
            self.turnplayer = self.player2
        else:
            self.turnplayer = self.player1

    # TO TAKE TURN
    def turn(self):

        pos = int(input("Enter Pos for {}".format(self.turnplayer)))
        if 0<pos<10:
            self.currentBord[pos - 1] = self.turnplayer
        else:
            self.changeTurn()



    # to check if player win or not

    def checkWin(self, mark = turnplayer):


        #all type of win conditions
        winConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                         [0, 4, 8], [2, 4, 6]]

        for condition in winConditions:
            win = 1
            for place in condition:
                if self.currentBord[place] != mark:
                    win = 0
            if win == 1:
                # some one wins so return their symbol
                return self.turnplayer

        drawCheck = 1
        for place in self.currentBord:
            if place == " ":
                drawCheck = 1
                #space is left and no one win
                return 0
        # if there is no white space remains and no player wins then draw
        return "Both player"
