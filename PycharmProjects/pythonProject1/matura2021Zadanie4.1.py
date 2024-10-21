file = open('przyklad2.txt', 'r')
rows = file.read()

howManyNumbers = 0
for row in rows :
    row = row.strip()
    for char in row :
        if char.isdigit() :
            howManyNumbers += 1

print(howManyNumbers)
