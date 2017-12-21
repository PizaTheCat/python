
def checkFunct( arg ):
    daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    theDaysFormatted = []
    f = open("2018CalendarV2.txt")
    with open("2018CalendarV2.txt",'r',encoding = 'utf-8') as f:
        for i in range(0, daysInEachMonth[arg]):
            theDaysFormatted.append(str(f.read(2)))
    temp1 = 0
    for i in range(0, arg):
        temp1 = temp1 + daysInEachMonth[i]
    temp1 = temp1 % 7
    temp2 = daysInEachMonth[arg]
    for i in range(0, temp2):
        temp1 += 1
        print(theDaysFormatted[i], end = '  ')
        if temp1 == 7:
            print("\n")
            temp1 = 0
def monthPrint( num ):
    if num == 1:
        checkFunct(num - 1)
    if num == 2:
        print("            ", end = '')
        checkFunct(num - 1)
    if num == 3:
        print("            ", end = '')
        checkFunct(num - 1)
    if num == 4:
        print("                        ", end = '')
        checkFunct(num - 1)
    if num == 5:
        print("    ", end = '')
        checkFunct(num - 1)
    if num == 6:
        print("                ", end = '')
        checkFunct(num - 1)
    if num == 7:
        print("                        ", end = '')
        checkFunct(num - 1)
    if num == 8:
        print("        ", end = '')
        checkFunct(num - 1)
    if num == 9:
        print("                    ", end = '')
        checkFunct(num - 1)
    if num == 10:
        checkFunct(num - 1)
    if num == 11:
        print("            ", end = '')
        checkFunct(num - 1)
    if num == 12:
        print("                    ", end = '')
        checkFunct(num - 1)
def calendarPrint( inputNum ):
    print( "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su", sep = '  ')
    monthPrint(inputNum)
inputM = input("Input the Month in numbers: ")
calendarPrint(int(inputM))
# First day of the year is Monday
