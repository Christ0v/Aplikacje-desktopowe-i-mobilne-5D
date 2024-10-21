file = open('przyklad2.txt', 'r')
rows = file.readlines()

password = ''
for row in rows:
    row = row.strip()
    optionOne = row + row[0]

    if optionOne == optionOne[::-1]:
        password += optionOne[len(optionOne)  // 2]

print(password)