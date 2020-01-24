import bord
b = bord.Bord()
b.setBord()
while 1:
    b.drawBord()
    b.turn()
    win = b.checkWin()
    if (win != 0):
        print("## {} wins ##".format(win))
        b.setBord()
    b.changeTurn()






