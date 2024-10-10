counter = 0
counterSecond = 0
file= open("przyklad.txt","r")
fileNumbers = file.read()
listOfNumbers = list(fileNumbers.split())
print(listOfNumbers)
print(set(listOfNumbers))
print(len(set(listOfNumbers)))
for i in range(len(listOfNumbers)):
    if listOfNumbers.count(listOfNumbers[i]) == 2:
        counter += 1

result = counter / 2
print(int(result))
for i in range(len(listOfNumbers)):
    if listOfNumbers.count(listOfNumbers[i]) == 3:
        counterSecond += 1

resultSecond = counterSecond / 2
print(int(resultSecond))