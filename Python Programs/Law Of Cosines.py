import math

def calculate():
    print("-----------------------------")

    sideOrAngle = raw_input("Are you solving for a side or angle?(s/a): ")

    if(sideOrAngle == 's'):
        knownAngle = float(input("Enter known angle: "))
        sideOne = float(input("Enter the first known side: "))
        sideTwo = float(input("Enter the second known side: "))

        result = math.sqrt(sideOne**2 + sideTwo**2 - (2 * sideOne * sideTwo) * math.cos(math.radians(knownAngle)))
        
    elif(sideOrAngle == 'a'):
        sideOne = float(input("Enter side opposite of unknown angle: "))
        sideTwo = float(input("Enter side 1: "))
        sideThree = float(input("Enter side 2: "))

        result = math.acos((sideOne**2 - sideTwo**2 - sideThree**2)/(-2 * sideTwo * sideThree))
        result = math.degrees(result)
        
    else:
        calculate()

    print("-----------------------------")

    print("\n\n----------RESULTS----------")

    print("\nAnswer: " + str(result))

    print("\n\n----------RESULTS----------")

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
