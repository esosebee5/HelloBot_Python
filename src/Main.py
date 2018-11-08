import datetime

# name = "copernicus"
name = ""
state = 0

def main():
    global name
    name = input("Enter your name: ")
    print()
    print("hello, " + name)
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
        print("Yay you chose 2")
    else:
        print ("Please decide.")

def clock():
    print("The time is ") 
    print(datetime.datetime.now())
    print()

def endProgram():
    global state
    state = 1
    print("User ended process.")

main()



