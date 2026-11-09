for i in range(10):
    print(i,end=" ")
print()
for i in range(2,10):
    print(i,end=" ")
print()
i = 2
print(i % 2 == 0)
for i in range(1,21):
    if i % 2 != 0:
        print(i,end=" ")
print()
''' your_float = float(input("Enter a float number: "))
print("Round to 2 decimals: {:.2f}".format(your_float))'''

'''money = input("How much to invest: ")
interest_rate = input("How much is interest rate: ")
money = float(money)
interest_rate = float(interest_rate) * 0.01

for i in range(10):
    money = money + (money * interest_rate)

print("Investment after 10 years: {:.2f}".format(money))'''

# i = 0.1 + 0.1 + 0.1 - 0.3
# print(i)

i = .1111111111111111111111111111111
j = .0000000000000010000000000000001
print("Answer: {:.32}".format(i+j))
print("3 + 4 * 5 = {}".format(3 + 4 * 5))
print("(3 + 4) * 5 = {}".format((3 + 4) * 5))

import random
random_number = random.randrange(1,51)

i = 1
''' while i != random_number:
    i+=1
print("The random value is: ",i) '''

''' while i <= 20:
    if i % 2 == 0:
        i = i + 1
        continue
    if i == 15:
        break
    print(i,end=" ")
    i+=1
'''

# How tall is the tree: 5
tree_height = int(input("How tall is the tree: "))
spaces = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(" ",end=' ')
    for i in range(hashes):
        print("#",end=" ")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(stump_spaces):
    print(" ",end=' ')
print("#")


