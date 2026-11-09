# single line comment
# another single line comment
'''
Multi line comment
Comments are ignored by compiler
Comments are helpful for understanding code
'''

# Ask the user to input their name and assign the input to a variable named "name"
''' name = input("What is your name? ")
print("Hello",name) '''

# Ask the user to input 2 values and assign those to 2 variables named num1 and num2
'''num1, num2 = input("Enter two numbers: ").split()
# Convert the strings into regular numbers Integer
num1 = int(num1)
num2 = int(num2)
# print arithmetic operations
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} // {num2} = {num1 // num2}") '''

# Problem: Receive miles and convert it to kilometers
# kilometers = miles * 1.60934
''' miles = int(input("Enter miles: "))
kilometers = miles * 1.60934
print("{} miles is {} kilometers".format(miles, kilometers)) '''

'''num1, num2, operator = input("Enter two numbers: ").split()

num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif operator == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
elif operator == "**":
    print(f"{num1} ** {num2} = {num1 ** num2}")
elif operator == "//":
    print(f"{num1} // {num2} = {num1 // num2}")
else:
    print("Invalid operator")'''

age = eval(input("Enter your age: "))
if (age >= 1) and (age <= 18):
    print("Important Birthday")
elif (age == 21) and (age == 50):
    print("Important Birthday")
elif not (age < 65):
    print("Important Birthday")
else:
    print("Not Important!")

if age < 5:
    print("Too young to go to school")
elif age == 5:
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
# Handle everyone else
else:
    print("Go to college")

import sys
print(sys.version_info)