def monthPrint( num ):
    if num == 1:
        print("    1   2   3   4   5   6 ")
        print("7   8   9   10  11  12  13")
        print("14  15  16  17  18  19  20")
        print("21  22  23  24  25  26  27")
        print("28  29  30  31")
    if num == 2:
        print("                1   2   3 ")
        print("4   5   6   7   8   9   10")
        print("11  12  13  14  15  16  17")
        print("18  19  20  21  22  23  24")
        print("25  26  27  28")
    if num == 3:
        print("                1   2   3 ")
        print("4   5   6   7   8   9   10")
        print("11  12  13  14  15  16  17")
        print("18  19  20  21  22  23  24")
        print("25  26  27  28  29  30  31")
    if num == 4:
        print("1   2   3   4   5   6   7 ")
        print("8   9   10  11  12  13  14")
        print("15  16  17  18  19  20  21")
        print("22  23  24  25  26  27  28")
        print("29  30")
    if num == 5:
        print("        1   2   3   4   5")
        print("6   7   8   9   10  11  12")
        print("13  14  15  16  17  18  19")
        print("20  21  22  23  24  25  26")
        print("27  28  29  30  31")
    if num == 6:
        print("                    1   2")
        print("3   4   5   6   7   8   9")
        print("10  11  12  13  14  15  16")
        print("17  18  19  20  21  22  23")
        print("24  25  26  27  28  29  30")
    if num == 7:
        print("1   2   3   4   5   6   7")
        print("8   9   10  11  12  13  14")
        print("15  16  17  18  19  20  21")
        print("22  23  24  25  26  27  28")
        print("29  30  31")
    if num == 8:
        print("            1   2   3   4")
        print("5   6   7   8   9   10  11")
        print("12  13  14  15  16  17  18")
        print("19  20  21  22  23  24  25")
        print("26  27  28  29  30  31")
    if num == 9:
        print("                        1")
        print("2   3   4   5   6   7   8")
        print("9   10  11  12  13  14  15")
        print("16  17  18  19  20  21  22")
        print("23  24  25  26  27  28  29")
        print("30")
    if num == 10:
        print("    1   2   3   4   5   6")
        print("7   8   9   10  11  12  13")
        print("14  15  16  17  18  19  20")
        print("21  22  23  24  25  26  27")
        print("28  29  30  31")
    if num == 11:
        print("                1   2   3")
        print("4   5   6   7   8   9   10")
        print("11  12  13  14  15  16  17")
        print("18  19  20  21  22  23  24")
        print("25  26  27  28  29  30")
    if num == 12:
        print("                        1")
        print("2   3   4   5   6   7   8")
        print("9   10  11  12  13  14  15")
        print("16  17  18  19  20  21  22")
        print("23  24  25  26  27  28  29")
        print("30  31")
def calendarPrint( inputNum ):
    print("Su","Mo","Tu","We","Th","Fr","Sa",sep='  ')
    monthPrint(inputNum)
inputM = input("Input the Month in numbers: ")
calendarPrint(int(inputM))