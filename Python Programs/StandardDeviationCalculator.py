# Imports math package
import math

def calculation():

    # Makes list to store all inputted numbers.
    numbers = []

    # Makes list to store numbers of standard deviation.
    standardDeviationList = []

    # Makes int to store the mean.
    mean = 0

    # Makes int to store the median
    median = 0

    # Makes int to store the range.
    theRange = 0

    # Makes float to store the standard deviation.
    standardDeviation = 0.0

    print("-----------------------------")

    # Asks the user how many numbers they wish to input.
    numberOfNumbers = input('How many numbers do you need to input?: ')

    print("-----------------------------")

    # Loops from 0 to the number of numbers(Inputted Above)
    for i in range(0, numberOfNumbers):
        # Asks for the user's input,
        userInput = input('Enter a number: ')
        # Adds the user's input to the 'numbers' list accordingly.
        numbers.append(userInput)

    # Sorts the numbers.
    numbers.sort()



    ##### Mean Calculation #####

    # Loops from 0 to number of numbers.
    for i in range(0, numberOfNumbers):
        
        # Adds the number at the specified index in the list to the mean variable.
        mean += numbers[i]
        
    # Casts the mean to a float, and stores the value of mean divided by numberOfNumbers into the mean varaible.
    # This is the final value of mean.
    mean = float(mean) / numberOfNumbers

    ##### Mean Calculation #####



    ##### Median Calculation #####

    # Checks if the amount of numbers is even or odd.
    # If even: 
    if(numberOfNumbers % 2 == 0):
        
        # Makes num1 equal to the number at the left side of the middle.
        num1 = float(numbers[numberOfNumbers / 2 - 1])
        
        # Makes num2 equal to the number at the right side of the middle.
        num2 = numbers[numberOfNumbers / 2]
        
        # Makes the meadian equal to the two numbers added together.
        median = num1 + num2
        
        # Makes the median equal to the median divided by 2.
        # This is the final value of median.
        median = median / 2
        
    # If odd:
    else:
        
        # Creates a middle variable, and makes it equal to numberOfNumbers divided by two, and removes the '.5' at the end to keep the number even.
        middle = float((numberOfNumbers / 2) - .5)
        
        # Makes the median equal to the number at the middle index of the numbers list.
        # This is the final value of median.
        median = numbers[int(middle) + 1]

    ##### Median Calculation #####


        
    ##### Range Calculation #####

    # Makes theRange equal to the last value of the numbers list minus the first value of the numbers list.
    # This is the final value of theRange.
    theRange = numbers[numberOfNumbers - 1] - numbers[0]

    ##### Range Calculation #####



    ##### Standard Deviation Calculation #####

    # Loops from 0 to number of numbers.
    for i in range(0, numberOfNumbers):
        # Subtracts the number at the current index of the list and the mean(calculated above),
        # and adds the absolute value of that number to the standardDeviationList.
        standardDeviationList.append(abs(numbers[i] - mean))
        
    # Loops from 0 to number of numbers.
    for i in range(0, numberOfNumbers):
        # Sqaures the number at the current index of the standardDeviationList
        standardDeviationList[i] = standardDeviationList[i]**2
        
    # Loops from 0 to number of numbers.
    for i in range(0, numberOfNumbers):
        # Makes the standardDeviation equal to the current value of standardDeviation plus the number at the current index of the standardDeviationList.
        standardDeviation += standardDeviationList[i]

    # Makes the standardDeviation equal to the sqaure root of standardDeviation divided by numberOfNumbers.
    standardDeviation = math.sqrt(standardDeviation / numberOfNumbers)

    ##### Standard Deviation Calculation #####

    print("\n\n----------RESULTS----------")

    # Prints everything.
    print("\nMean: " + str(mean) + "\n\nMedian: " + str(median) + "\n\nRange: " + str(theRange) + "\n\nStandard Deviation: " + str(standardDeviation) + "\n")

    print("----------RESULTS----------")

notDone = True

while(notDone):
    x = ''
    calculation()
    x = raw_input("Calculate Again? (Y/N): ")
    if(x == 'y'):
        notDone = True
    else:
        notDone = False

input("\n\n---------------------------\nPress ENTER to exit program\n---------------------------")
