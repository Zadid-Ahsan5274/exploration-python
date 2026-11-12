import os

with open("mydata.txt",mode="w",encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more random text")

with open("mydata.txt",encoding="utf-8") as myFile:
    print(myFile.read())
print(myFile.closed)
print(myFile.name)
print(myFile.mode)
# os.rename("mydata.txt","mydata2.txt")
# os.replace("mydata.txt", "mydata2.txt")
# os.remove("mydata2.txt")
os.mkdir("my_directory")
os.chdir("my_directory")
print("Get current directory: ",os.getcwd())
os.chdir("..")
print("Get current directory: ",os.getcwd())
os.rmdir("my_directory")

with open("mydata2.txt",encoding="utf-8") as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break
        print("line: ",lineNum)
        wordList = line.split()
        # print("line",lineNum," : ",line,end="")
        print("Number of words: ",len(wordList))
        charCount = 0
        for word in wordList:
            for char in word:
                charCount += 1
        avgNumChars = charCount/len(wordList)
        print("Average word length: {:.2}".format(avgNumChars))
        lineNum += 1

myTuple = (1,2,3,5,8)
print("first value: ", myTuple[0])
print(myTuple[0:3])
print("Tuple Length: ",len(myTuple))
moreFibs = myTuple + (13,21,34)
print("32 in tuple: ",32 in moreFibs)

for i in moreFibs:
    print(i)

aList = [55,89,144]
aTuple = tuple(aList)
aList = list(aTuple)
print("Min : ",min(aTuple))
print("Max : ",max(aTuple))
