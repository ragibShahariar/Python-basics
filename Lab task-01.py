"""Printing data"""
print("Hello world") # printing hello world to the display

name = "Ragib Shahariar" # name is a variable stores String type data
print(name) # print function now printing a content of the variable

# we can print any data using print() function
# let's print an Integer number
print (100)
# also a fractional number which called double data type in python
grade = 3.89
print(grade)

"""let's do arithmetic operation between two numbers"""
price_of_theBook = 500
price_of_the_pen = 5

total_price = price_of_theBook + price_of_the_pen
print("total price = ",total_price) # we can put various data types value
                                    # in the print() function
                                    # we have to use `,` (comma) operator
                                    # regardless it is a variable or direct value
"""taking input in python"""
name = input("enter your name: ") # input() function read data from the user and wait's to have input
print("Hello ", name) # by default input() takes value's as String data type
                      # for number input we have to convert it to number.

num1 = int(input("enter a number: ")) # taking number one and convert to Integer data
num2 = int(input("enter 2'nd number: "))# taking number two and convert to Integer data

operation = input("enter operation (+,-,x,/) : ")

"""operators and conditional logic"""
if operation in ['+', '-', 'x', '/']:
    if operation == '+':
        print(num1 + num2) # used + operator for addition
    if operation == '-':
        print(num1 - num2) # used - operator for addition
    if operation == 'x':
        print(num1 * num2) # used * operator for addition
    if operation == '/':
        print(num1 / num2) # used / operator for addition
else:
    print("invalid operator.")

"""Looping while loop"""
condition_flag = 1
while condition_flag: # while(1) means true always and while(0) means always false unless the value of 1/0 changes
    operation = input("enter operation +,-,x,/ (0 to exit): ")
    if operation == '0':     # if user gives 0 then condition_flag will be 0 (false) which breaks the loop
        condition_flag = 0
    if operation not in ['+', '-', 'x', '/']:
        print("Invalid operation try again...")
        continue # if user gives something that are not matches with the operator code will be start from the loop again
    else:
        num1 = int(input("enter a number: "))  # taking number one and convert to Integer data
        num2 = int(input("enter 2'nd number: "))# taking number two and convert to Integer data
        if operation == '+':
            print(num1 + num2)  # used + operator for addition
        if operation == '-':
            print(num1 - num2)  # used - operator for addition
        if operation == 'x':
            print(num1 * num2)  # used * operator for addition
        if operation == '/':
            print(num1 / num2)  # used / operator for addition

"""Looping for loop"""

for i in range(1,11,1): # inside range 1'st 1 is initialization last 1 is increment rate and 11 is the range before 11
    print(i," Bangladesh")

"""function"""

def multiplicationTable(num = 1): # we have to manually call the function to execute it. it takes one parameter.
    for i in range(1, 11):
        print(i, " x ", num, " = ", i*num)

number = 5
multiplicationTable(number)


