import datetime

# name = "copernicus"
name = ""
state = 0

def main():
    global name
    name = input("Enter your name: ")
    print()
    print("Hello, " + name + ".")
    print()

    while state == 0:
        userInput = input("Enter '1' for Clock, '2' to Calculate Age, or\n" +
                    "enter 'end' to terminate: ")
        print()
        chooseProgram(userInput)

def chooseProgram(var):
    if var == "end":
        endProgram()
    elif var == "1":
        clock()
    elif var == "2":
        calculateAge()
        print()
    else:
        print ("Please decide.")

def clock():
    dt = datetime.datetime.now().time()
    dt_hour = dt.__str__()
    time_arr = dt_hour.split('.')
    time = time_arr[0]
    startApp()
    print("The current time is " + time)
    endApp()
    print()

def calculateAge():
    month = 0
    while month < 1:
        monthString = input("Enter your birth month: ")
        month = getMonth(monthString)
    print(month)

def startApp():
    print("--------------------------------")

def endApp():
    print("--------------------------------")

def endProgram():
    global state
    state = 1
    print("User ended process.")

def getMonth(var):
    monthStr = str(var).lower()
    if monthStr == "january" or monthStr == "jan":
        return 1
    elif monthStr == "february" or monthStr == "feb":
        return 2
    elif monthStr == "march" or monthStr == "mar":
        return 3
    elif monthStr == "april" or monthStr == "apr":
        return 4
    elif monthStr == "may":
        return 5
    elif monthStr == "june" or monthStr == "jun":
        return 6
    elif monthStr == "july" or monthStr == "jul":
        return 7
    elif monthStr == "august" or monthStr == "aug":
        return 8
    elif monthStr == "september" or monthStr == "sep":
        return 9
    elif monthStr == "october" or monthStr == "oct":
        return 10
    elif monthStr == "november" or monthStr == "nov":
        return 11
    elif monthStr == "december" or monthStr == "dec":
        return 12
    else:
        return 0

main()

