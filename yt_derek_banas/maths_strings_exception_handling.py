# Exception Handling
'''
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("You did not enter a number")
    except:
        print("An unknown error occured")
print("Thank you for entering a number. You entered {}".format(number)) '''
# Exception Handling

# while loop
'''secret_number = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("You guessed the number")
        break'''

# import math

''' print("ceil(4.4) = {}".format(math.ceil(4.4)))
print("floor(4.4) = {}".format(math.floor(4.4)))
print("fabs(-4.4) = {}".format(math.fabs(-4.4)))
print("factorial(4) = {}".format(math.factorial(4)))
print("fmod(5,4) = {}".format(math.fmod(5,4)))
print("trunc(4.2) = {}".format(math.trunc(4.2)))
print("pow(2,2) = {}".format(math.pow(2,2)))
print("sqrt(9) = {}".format(math.sqrt(9)))
print("math.e = {}".format(math.e))
print("math.log(20) = {}".format(math.log(20)))
print("math.pi = {}".format(math.pi))
print("exp(4) = {}".format(math.exp(4)))
print("log(1000,10) = {}".format(math.log(1000,10)))
print("log10(1000) = {}".format(math.log10(1000)))
print("degrees(1.5708) = {}".format(math.degrees(1.5708)))
print("radians(90) = {}".format(math.radians(90))) '''

from decimal import Decimal as D

sum = D(0)
sum += D(0.1)
sum += D(0.1)
sum += D(0.1)
sum -= D(0.3)
print(f"Sum = {sum}")
print("0.1 + 0.1 + 0.1 - 0.3 = ",(0.1 + 0.1 + 0.1 - 0.3))

print(type(3))
print(type(3.145))
print(type("3"))
print(type('3'))

sample_string = "This is a very import string"
print(sample_string[0])
print(sample_string[-1])
print(sample_string[3+5])
print("Length : {}".format(len(sample_string)))
print(sample_string[0:4])
print(sample_string[4:])
print(sample_string[:8])
print("Green "+"Eggs")
print("Hello "*5)
num_string = str(11)

for char in sample_string:
    print(char,end=" ")
print()

for i in range(0, len(sample_string)-1,2):
    print(sample_string[i]+sample_string[i+1],end="")
print()
print("A = ",ord("A"))
print("65 = ",chr(65))

normal_string = input("Enter a string to hide in uppercase: ")
secret_string = ""
for char in normal_string:
    secret_string = secret_string + str(ord(char)-23)

print("secret message : ",secret_string)
normal_string = ""
for i in range(0,len(secret_string)-1,2):
    char_code = secret_string[i]+secret_string[i+1]
    normal_string += chr(int(char_code)+23)
print("Original message: ",normal_string)

