def add_numbers(num1,num2):
    return num1+num2

print("5 + 4 = ",add_numbers(5,4))

def assign_name():
    name = "Duog"

# print(name) -> shows error

global_name = "Sally"

def change_name():
    global global_name
    global_name = "Sammy"

# name = "Tom"
# name = change_name(name)
change_name()

print(global_name)

def get_sum(num1,num2):
    sum = num1 + num2

print(get_sum(5,4))

def solve_equation(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = "+str(num2-num1)

print(solve_equation("x + 4 = 9"))

def mult_divide(num1, num2):
    return (num1*num2),(num1/num2)

mult, divide = mult_divide(5,4)
print("5 * 4 = ",mult)
print("5 / 4 = ",divide)

# check prime
'''def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_primes(max_number):
    list_of_primes = []
    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes

max_number_to_check = int(input("Search for primes up to: "))
list_of_primes = get_primes(max_number_to_check)

for prime in list_of_primes:
    print(prime,end=" ")
print() '''

def sum_all(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print("Sum: {}".format(sum_all(1,2,3,4,5,6,7,8,9)))

import math

def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length*width
    print("The area of the rectangle: ",area)

def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi*(math.pow(radius,2))
    print("The area of the circle is {:.2f}: ".format(area))

def main():
    shape_type = input("Get area for what shape: ")
    get_area(shape_type)

main()