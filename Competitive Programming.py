print("Palindrome Detector")

#using 'try' function to handle exceptions in case of ValueErrors

try:

#limit the input to integers and assign its value to variable 'n'

    n=int(input("Enter a number here."))

#slicing the int 'n' by making it a str first. Using ‘palindrome’ word as a variable for the value of palindrome of ‘n’

    palindrome=str(n)[::-1]

#using Conditionals 'if' and 'else' to get the desired output.

    if palindrome==str(n):
        print("True")
        print("Explanation: as the palindrome of the number is" , palindrome + ".")
    else:
        print("False")
        print ("Explanation: as the palindrome of the number is" , palindrome + ".")

#to handle the exception

except ValueError:	
    print ("Invalid input. Please enter a number here.")
