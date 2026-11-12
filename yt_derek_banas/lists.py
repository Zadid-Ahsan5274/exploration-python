import math, random

''' randList = ["string",1.234,28]
oneToTen = list(range(10))
randList = randList + oneToTen
print(randList[0])
print("List Length: {}".format(len(randList)))
first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print(first3[0]*3)
print("string " in first3)
print("String index:" ,first3.index("string"))
print("How many strings :",first3.count("string"))

first3[0] = "New string"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

first3.append("Another random string")

for i in first3:
    print("{} : {}".format(first3.index(i), i))


numList = []
for i in range(5):
    numList.append(random.randrange(1,10))
for i in numList:
    print(i,end=" ")
print()
numList.insert(5,10)
numList.remove(10)
numList.pop(2)
for i in numList:
    print(i,end=" ")
print()
# print("Sorted-----")
# numList.sort()
# print("Reversed-----")
# numList.reverse()

for i in numList:
    print(i,end=" ")
print()
i = len(numList) - 1
while i > 1:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(numList[j], numList[j+1]))
        if numList[j] > numList[j+1]:
            print("Switch")
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't switch")
        j+=1
        for k in numList:
            print(k, end=",")
        print()
    print("END OF ROUND")
    i -= 1
for k in numList:
    print(k, end=",")
print() '''

evenList = [i*2 for i in range(10)]
for i in evenList:
    print(i, end=" ")
print()

numList = [1,2,3,4,5]
listOfValues = [[math.pow(m,2),math.pow(m,3),math.pow(m,4)]
                for m in numList]

for i in listOfValues:
    print(i, end=" ")
print()

multiDList = [[0] * 10 for i in range(10)]
multiDList[0][1] = 10
print(multiDList[0][1])
print(multiDList[1][1])

listTable = [[0] * 4 for i in range(4)]
for i in range(4):
    for j in range(4):
        listTable[i][j] = "{} : {}".format(i,j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=" || ")
    print()
print("------------------------")

multiDTable = [[0] * 10 for i in range(10)]

for i in range(1,10):
    for j in range(1,10):
        multiDTable[i][j] = i*j

for i in range(1,10):
    for j in range(1,10):
        print(multiDTable[i][j], end=" || ")
    print()