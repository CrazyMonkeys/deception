import main
import time



def getGame1():
    myGame = main.game()
    myGame.board.setContent([3,3], main.cellStatus.LIGHT)
    myGame.board.setContent([3,4], main.cellStatus.LIGHT)
    myGame.board.setContent([3,5], main.cellStatus.LIGHT)
    myGame.board.setContent([3,6], main.cellStatus.LIGHT)
    myGame.board.setContent([3,7], main.cellStatus.LIGHT)
    myGame.board.setContent([3,8], main.cellStatus.LIGHT)
    myGame.board.setContent([3,9], main.cellStatus.LIGHT)
    myGame.board.setContent([3,10], main.cellStatus.LIGHT)
    myGame.board.setContent([4,10], main.cellStatus.LIGHT)
    myGame.board.setContent([4,11], main.cellStatus.LIGHT)
    myGame.board.setContent([3,11], main.cellStatus.LIGHT)
    myGame.board.setContent([3,12], main.cellStatus.LIGHT)
    myGame.board.setContent([4,12], main.cellStatus.LIGHT)
    myGame.board.setContent([5,12], main.cellStatus.LIGHT)
    myGame.board.setContent([6,12], main.cellStatus.LIGHT)
    myGame.board.setContent([7,12], main.cellStatus.LIGHT)
    myGame.board.setContent([8,12], main.cellStatus.LIGHT)
    myGame.board.setContent([9,12], main.cellStatus.LIGHT)
    myGame.board.setContent([9,13], main.cellStatus.LIGHT)
    myGame.board.setContent([9,14], main.cellStatus.LIGHT)
    myGame.board.setContent([9,14], main.cellStatus.LIGHT)
    myGame.board.setContent([10,14], main.cellStatus.LIGHT)
    myGame.board.setContent([10,3], main.cellStatus.LIGHT)
    myGame.board.setContent([10,4], main.cellStatus.LIGHT)
    myGame.board.setContent([10,5], main.cellStatus.LIGHT)
    myGame.board.setContent([10,6], main.cellStatus.LIGHT)
    myGame.board.setContent([10,7], main.cellStatus.LIGHT)
    myGame.board.setContent([10,8], main.cellStatus.LIGHT)
    myGame.board.setContent([9,3], main.cellStatus.LIGHT)
    myGame.board.setContent([9,4], main.cellStatus.LIGHT)
    myGame.board.setContent([9,5], main.cellStatus.LIGHT)
    myGame.board.setContent([9,6], main.cellStatus.LIGHT)
    myGame.board.setContent([20,3], main.cellStatus.LIGHT)
    myGame.board.setContent([20,4], main.cellStatus.LIGHT)
    myGame.board.setContent([20,5], main.cellStatus.LIGHT)
    myGame.board.setContent([20,6], main.cellStatus.LIGHT)
    myGame.board.setContent([20,7], main.cellStatus.LIGHT)
    myGame.board.setContent([20,8], main.cellStatus.LIGHT)
    myGame.board.setContent([20,9], main.cellStatus.LIGHT)
    myGame.board.setContent([20,10], main.cellStatus.LIGHT)
    myGame.board.setContent([20,11], main.cellStatus.LIGHT)
    myGame.board.setContent([20,12], main.cellStatus.LIGHT)
    myGame.board.setContent([21,12], main.cellStatus.LIGHT)
    myGame.board.setContent([21,13], main.cellStatus.LIGHT)
    myGame.board.setContent([21,14], main.cellStatus.LIGHT)
    return myGame
    
def getGame2():
    myGame = main.game()
    myGame.board.setContent([2,0], main.cellStatus.LIGHT)
    myGame.board.setContent([2,1], main.cellStatus.LIGHT)
    myGame.board.setContent([2,2], main.cellStatus.LIGHT)
    myGame.board.setContent([2,3], main.cellStatus.LIGHT)
    myGame.board.setContent([2,4], main.cellStatus.LIGHT)
    myGame.board.setContent([2,5], main.cellStatus.LIGHT)
    myGame.board.setContent([2,6], main.cellStatus.LIGHT)
    myGame.board.setContent([2,7], main.cellStatus.LIGHT)
    myGame.board.setContent([2,8], main.cellStatus.LIGHT)
    myGame.board.setContent([2,9], main.cellStatus.LIGHT)
    myGame.board.setContent([2,10], main.cellStatus.LIGHT)
    myGame.board.setContent([2,11], main.cellStatus.LIGHT)
    myGame.board.setContent([2,12], main.cellStatus.LIGHT)
    myGame.board.setContent([3,13], main.cellStatus.LIGHT)
    myGame.board.setContent([4,14], main.cellStatus.LIGHT)
    myGame.board.setContent([5,14], main.cellStatus.LIGHT)
    myGame.board.setContent([5,0], main.cellStatus.LIGHT)
    myGame.board.setContent([6,0], main.cellStatus.LIGHT)
    myGame.board.setContent([7,0], main.cellStatus.LIGHT)
    myGame.board.setContent([8,0], main.cellStatus.LIGHT)
    myGame.board.setContent([9,0], main.cellStatus.LIGHT)
    myGame.board.setContent([10,0], main.cellStatus.LIGHT)
    myGame.board.setContent([11,0], main.cellStatus.LIGHT)
    myGame.board.setContent([12,0], main.cellStatus.LIGHT)
    myGame.board.setContent([13,0], main.cellStatus.LIGHT)
    myGame.board.setContent([14,0], main.cellStatus.LIGHT)
    myGame.board.setContent([15,0], main.cellStatus.LIGHT)
    myGame.board.setContent([16,0], main.cellStatus.LIGHT)
    myGame.board.setContent([17,1], main.cellStatus.LIGHT)
    myGame.board.setContent([18,2], main.cellStatus.LIGHT)
    myGame.board.setContent([19,3], main.cellStatus.LIGHT)
    myGame.board.setContent([20,4], main.cellStatus.LIGHT)
    myGame.board.setContent([21,5], main.cellStatus.LIGHT)
    myGame.board.setContent([22,6], main.cellStatus.LIGHT)
    myGame.board.setContent([23,6], main.cellStatus.LIGHT)
    myGame.board.setContent([23,7], main.cellStatus.LIGHT)
    myGame.board.setContent([23,8], main.cellStatus.LIGHT)
    myGame.board.setContent([23,9], main.cellStatus.LIGHT)
    myGame.board.setContent([24,6], main.cellStatus.LIGHT)
    myGame.board.setContent([24,7], main.cellStatus.LIGHT)
    myGame.board.setContent([24,8], main.cellStatus.LIGHT)
    myGame.board.setContent([24,9], main.cellStatus.LIGHT)
    myGame.board.setContent([25,6], main.cellStatus.LIGHT)
    myGame.board.setContent([25,7], main.cellStatus.LIGHT)
    myGame.board.setContent([25,8], main.cellStatus.LIGHT)
    myGame.board.setContent([25,9], main.cellStatus.LIGHT)
    myGame.board.setContent([24,9], main.cellStatus.LIGHT)
    myGame.board.setContent([23,9], main.cellStatus.LIGHT)
    myGame.board.setContent([22,9], main.cellStatus.LIGHT)
    myGame.board.setContent([21,9], main.cellStatus.LIGHT)
    myGame.board.setContent([20,9], main.cellStatus.LIGHT)
    myGame.board.setContent([19,9], main.cellStatus.LIGHT)
    myGame.board.setContent([18,9], main.cellStatus.LIGHT)
    myGame.board.setContent([17,9], main.cellStatus.LIGHT)
    myGame.board.setContent([16,9], main.cellStatus.LIGHT)
    myGame.board.setContent([15,9], main.cellStatus.LIGHT)
    myGame.board.setContent([14,9], main.cellStatus.LIGHT)
    myGame.board.setContent([13,9], main.cellStatus.LIGHT)
    myGame.board.setContent([12,9], main.cellStatus.LIGHT)
    myGame.board.setContent([11,9], main.cellStatus.LIGHT)
    myGame.board.setContent([10,9], main.cellStatus.LIGHT)
    myGame.board.setContent([9,9], main.cellStatus.LIGHT)
    myGame.board.setContent([8,9], main.cellStatus.LIGHT)
    myGame.board.setContent([7,9], main.cellStatus.LIGHT)
    myGame.board.setContent([6,9], main.cellStatus.LIGHT)
    myGame.board.setContent([5,9], main.cellStatus.LIGHT)
    myGame.board.setContent([4,9], main.cellStatus.LIGHT)
    myGame.board.setContent([25,7], main.cellStatus.LIGHT)
    myGame.board.setContent([24,7], main.cellStatus.LIGHT)
    myGame.board.setContent([23,7], main.cellStatus.LIGHT)
    myGame.board.setContent([22,7], main.cellStatus.LIGHT)
    myGame.board.setContent([21,7], main.cellStatus.LIGHT)
    myGame.board.setContent([20,7], main.cellStatus.LIGHT)
    myGame.board.setContent([19,7], main.cellStatus.LIGHT)
    myGame.board.setContent([18,7], main.cellStatus.LIGHT)
    myGame.board.setContent([17,7], main.cellStatus.LIGHT)
    myGame.board.setContent([16,7], main.cellStatus.LIGHT)
    myGame.board.setContent([15,7], main.cellStatus.LIGHT)
    myGame.board.setContent([14,7], main.cellStatus.LIGHT)
    myGame.board.setContent([13,7], main.cellStatus.LIGHT)
    myGame.board.setContent([12,7], main.cellStatus.LIGHT)
    myGame.board.setContent([11,7], main.cellStatus.LIGHT)
    myGame.board.setContent([10,7], main.cellStatus.LIGHT)
    myGame.board.setContent([9,7], main.cellStatus.LIGHT)
    myGame.board.setContent([8,7], main.cellStatus.LIGHT)
    myGame.board.setContent([7,7], main.cellStatus.LIGHT)
    myGame.board.setContent([6,7], main.cellStatus.LIGHT)
    myGame.board.setContent([5,7], main.cellStatus.LIGHT)
    myGame.board.setContent([4,7], main.cellStatus.LIGHT)
    myGame.board.setContent([4,8], main.cellStatus.LIGHT)
    myGame.board.setContent([4,7], main.cellStatus.LIGHT)
    myGame.board.setContent([4,6], main.cellStatus.LIGHT)
    myGame.board.setContent([4,5], main.cellStatus.LIGHT)
    myGame.board.setContent([4,4], main.cellStatus.LIGHT)
    myGame.board.setContent([4,3], main.cellStatus.LIGHT)
    myGame.board.setContent([4,2], main.cellStatus.LIGHT)



    return myGame

print("setup position")

aGamelist = []
aGamelist.append(getGame2())
aGamelist.append(getGame1())

for myGame in aGamelist:

    myGame.setMyPosition(7, 10)
    drone = 3
    round = 0


    while 1:

        print("=========== Round", round, "===============")
        round += 1
        #Collet the inputs
        start_time = time.time()
        #helper_bots = int(raw_input())

        #for i in xrange(player_count):
        #    x, y = [int(j) for j in raw_input().split()]
        #    if x > -1:
            # real player have x,y > 0
        #        if i == my_id:
        #            myGame.setMyPosition(x, y)
        #        else:
        #            myGame.refreshPosition(x, y)
        #removal_count = int(raw_input())
        #for i in xrange(removal_count):
        #    remove_x, remove_y = [int(j) for j in raw_input().split()]
        #    myGame.refreshRemovePosition([remove_x, remove_y])


        myGame.applyPosition()
        myGame.board.printObject()

        retour = main.miniMax.miniMax(myGame, 4)
        #print >> sys.stderr, "Debug messages...", retour

        #theWinMove = miniMax.miniMax(myGame)
        end_time = time.time()

        print("Debug messages...", end_time-start_time)

        print( main.getLabel(retour.value))

        if retour.value == main.actions.DEPLOY:
            drone -= 1
            if drone < 0:
                print("GAME OVER LOOSERS")
                break


        myGame.applyRefresh(retour)

        myGame.myPosition = retour.getNewCoord(myGame.myPosition)




        # Write an action using print
        # To debug: print >> sys.stderr, "Debug messages..."