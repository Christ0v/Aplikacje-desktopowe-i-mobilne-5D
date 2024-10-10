file = open("przyklad.txt","r")
fileNumbers = file.read()

fileNumbers = fileNumbers[::-1]
numbers = list(fileNumbers.split())
print(numbers)

for i in range(len(numbers)):

    if int(numbers[i]) % 17 == 0:
        print(numbers[i])