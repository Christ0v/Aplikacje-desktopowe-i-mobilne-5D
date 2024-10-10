

file =open("przyklad.txt","r")
fileNumbers = file.read()
listOfNumbers = list(fileNumbers.split())
print(listOfNumbers)
def isFirst(number):

    for x in range(2,number//2):
        if number % x == 0:
            return False
    return True

reversedNumbers = list(fileNumbers[::-1].split())[::-1]
print(reversedNumbers)
for x in range(len(listOfNumbers)):
    if isFirst(int(listOfNumbers[x])) and isFirst(int(reversedNumbers[x])):
        print(listOfNumbers[x])