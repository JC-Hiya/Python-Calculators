def calculate():

    print("-----------------------------")
    
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    e = float(input("Enter E: "))
    f = float(input("Enter F: "))

    print("-----------------------------")

    xNum = (c * e) - (b * f)
    yNum = (a * f) - (c * d)
    den = (a * e) - (b * d)

    x = xNum / den
    y = yNum / den

    print("\n\n----------RESULTS----------")

    print("\nX: " + str(x) + "\nY: " + str(y))

    print("\n----------RESULTS----------\n")

notDone = True

while(notDone):
    n = ''
    calculate()
    n = raw_input("Calculate Again? (Y/N): ")
    if(n == 'y'):
        notDone = True
    else:
        notDone = False

input("\n\n---------------------------\nPress ENTER to exit program\n---------------------------")

