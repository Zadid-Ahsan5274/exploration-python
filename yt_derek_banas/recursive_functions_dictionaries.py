derekDictionary = {"fName":"Derek","lName":"Banas","address":"123 Main St"}
print("My Name is {}".format(derekDictionary["fName"]))
derekDictionary["address"] = "215 North St"
print(derekDictionary)
derekDictionary["city"] = "Pittsburgh"
print("Is there a city: ","city" in derekDictionary)
print(derekDictionary.values())
print(derekDictionary.keys())

for k,v in derekDictionary.items():
    print(k,v)
print(derekDictionary.get("lName","Not Here"))
del derekDictionary["fName"]

for k,v in derekDictionary.items():
    print(k,v)

derekDictionary.clear()
''' employees = []
fName,lName = input("Enter employee name: ").split()
employees.append({"fName": fName, "lName": lName})
print(employees) '''

''' customers = []
while True:
    createEntry = input("Enter Customer (Y/N)?: ")
    createEntry = createEntry[0].lower()

    if createEntry == 'n':
        break

    else:
        fName, lName = input("Enter customer name: ").split()
        customers.append({"fName": fName, "lName": lName})

for customer in customers:
    print(customer['fName'], customer['lName']) '''

# factorial
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result

print("4! = ",factorial(5))

# fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))

# Ask how many numbers they want?
numberFibValues = int(input("How many fibonacci values should be found: "))

i = 1
while i < numberFibValues:
    fibValue = fibonacci(i)
    print(fibValue)
    i += 1
print("All Done")