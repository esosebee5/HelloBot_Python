import datetime

# class Main:

####################
# GLOBAL VARIABLES #
####################

name = ""
state = True

########
# MAIN #
########

def main():
    global name
    name = input("Enter your name: ")
    print()
    print("Hello, " + name + ".")
    print()

    while state == True:
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

#########
# CLOCK #
#########

def clock():
    dt = datetime.datetime.now().time()
    dt_hour = dt.__str__()
    time_arr = dt_hour.split('.')
    time = time_arr[0]
    startApp()
    print("The current time is " + time)
    endApp()
    print()

#################
# CALCULATE AGE #
#################

def calculateAge():
    startApp()
    month,days_in_month = getMonth()
    day = getDay(days_in_month)
    year = getYear()
    # print(month, days_in_month)
    # print(day)
    # print(year)
    current_month,current_day,current_year = getCurrentMonthDayYearTuple()
    # print(current_month, current_day, current_year)

    # see if birthday has already come in the current year
    already_had_birthday = True
    days_till = 0
    months_till = 0
    if month >= current_month and day >= current_day:
        already_had_birthday = False
        days_till = day - current_day
        months_till = month - current_month

    # calculate age
    age = current_year - year
    if already_had_birthday:
        print("You are",age,"years old.")
    else:
        age = age - 1
        print("You are",age,"years old.")
        print("Your next birthday is in",months_till,
            "months and",days_till,"days.")
    endApp()

def getCurrentMonthDayYearTuple():
    return getCurrentMonth(),getCurrentDay(),getCurrentYear()

def getMonth():
    month = 0
    # days = 0
    while month < 1:
        monthString = input("Enter your birth month: ")
        month,days = getMonthNumber(monthString)
    return month,days

def getDay(num_days):
    day = 0
    if num_days == 28:
        num_days = num_days + 1
    while day < 1 or day > num_days:
        day_str = input("Enter a valid day of the month: ")
        day = getIsInt(day_str)
    return day

def getYear():
    year = 0
    # days = 0
    while year < 1:
        year_str = input("Enter your birth year: ")
        year = getIsInt(year_str)
    return year

def getIsInt(str_val):
    ret_val = 0
    try:
        ret_val = int(str_val)
    except ValueError:
        print("Enter a number.")
    finally:
        return ret_val

def getCurrentDateString():
    yr = datetime.datetime.now().date()
    yr_str = yr.__str__()
    return yr_str

def getCurrendDateArr():
    date_arr = getCurrentDateString().split("-")
    return date_arr

def getCurrentYear():
    date_arr = getCurrendDateArr()
    return int(date_arr[0])

def getCurrentMonth():
    return int(getCurrendDateArr()[1])

def getCurrentDay():
    return int(getCurrendDateArr()[2])

def getMonthNumber(var):
    monthStr = str(var).lower()
    if monthStr == "january" or monthStr == "jan":
        return 1,31
    elif monthStr == "february" or monthStr == "feb":
        year = float(getCurrentYear())
        if year / 4 == 0.0:
            return 2,29
        return 2,28
    elif monthStr == "march" or monthStr == "mar":
        return 3,31
    elif monthStr == "april" or monthStr == "apr":
        return 4,30
    elif monthStr == "may":
        return 5,31
    elif monthStr == "june" or monthStr == "jun":
        return 6,30
    elif monthStr == "july" or monthStr == "jul":
        return 7.31
    elif monthStr == "august" or monthStr == "aug":
        return 8,31
    elif monthStr == "september" or monthStr == "sep":
        return 9,30
    elif monthStr == "october" or monthStr == "oct":
        return 10,31
    elif monthStr == "november" or monthStr == "nov":
        return 11,30
    elif monthStr == "december" or monthStr == "dec":
        return 12,31
    else:
        return 0

##########################
# General shared methods #
##########################

def startApp():
    print("--------------------------------")

def endApp():
    print("--------------------------------")

def endProgram():
    global state
    state = False
    print("User ended process.")

#############
# EXECUTION #
#############

main()

