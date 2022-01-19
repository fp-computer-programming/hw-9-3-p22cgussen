# Author: CCG 12/9/21


while True:
    try: 
        temp = float(input("Enter the temperature: "))
        type = input("Do you want to convert to (f/C)?")
        if type.upper() == "C":
            result = (temp - 32) * 5 / 9
            print("{0} degrees farenheit is {1} degrees celcius.".format(temp, result))
        elif type.upper() == "F":
            result = temp / 5 * 9 + 32
            print("{0} degrees celcius is {1} degrees fahrenheit.".format(temp, result))
        else:
            print("Invalid input, enter F for fahrenheit or C for celsius.")
    except ValueError:
        print("Invalid input, enter a numerical value for the temperature")

