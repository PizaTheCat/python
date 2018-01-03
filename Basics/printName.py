
def printGlenn ():
    import datetime
    yesOrNo = input("Initialise? (Yes or No): ")
    if yesOrNo == "Yes":
        print("Initialising")
        print(".............GGGGGGGGGGGG..........LL.................EEEEEEEEEEEE..NN................NN...NN................NN")
        print(".........GGGG............GGG......LL.................EE............NNN...............NN...NNN...............NN")
        print("......GGG..................GG....LL.................EE............NN..N.............NN...NN..N.............NN")
        print("....GG......................G...LL.................EE............NN....N...........NN...NN....N...........NN")
        print("..G............................LL.................EEEEEEEEEE....NN......N.........NN...NN......N.........NN")
        print(".G.....................GGGGGG.LL.................EE............NN........N.......NN...NN........N.......NN")
        print(".G......................GG...LL.................EE............NN..........N.....NN...NN..........N.....NN")
        print("GG....................GG....LL.................EE............NN............N...NN...NN............N...NN")
        print("GGG.............GGGG.......LL.................EE............NN..............N.NN...NN..............N.NN")
        print(".GGGGGGGGGGGGGG...........LLLLLLLLLLLLLLLL...EEEEEEEEEEEE..NN...............NNN...NN...............NNN")
        print("Date and Time: " + str(datetime.datetime.now()))
    else:
        print("Date and Time: " + str(datetime.datetime.now()))
