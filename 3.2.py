# This is Problem 2

while True:

    try:

        choice = input("Press 1 to convert from Fahrenheit to Celsius or Press 2 to convert from Celsius to Fahrenheit, Press 3 to stop the program. ")

        if float(choice)==3:
            break
        else:
            print ("")
            temp = input("What is the number that you would like to convert? ")
            if float(choice)==1:
                temp = (float(temp) - 32) * 5 / 9
                print ("Your temperature in Celsius is: %s C." %temp)

            elif float(choice)==2:
                temp = float(temp) * 9/5 + 32
                print ("Your temperature in Fahrenheit is: %s F." %temp)

            else:
                print ("PLEASE ENTER EITHER 1 OR 2 OR 3!")

        print ("")

    except ValueError:
        print("")
        print ("INVALID INPUT! TRY AGAIN")
        print("")
