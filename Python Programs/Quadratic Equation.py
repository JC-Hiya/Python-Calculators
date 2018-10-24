import math

def calculate():
    print("-----------------------------")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    print("-----------------------------")

    posResult = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
    negResult = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)

    print("\n\n----------RESULTS----------")

    print("\nPositive Result: " + str(posResult) + "\nNegative Result: " + str(negResult))

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
