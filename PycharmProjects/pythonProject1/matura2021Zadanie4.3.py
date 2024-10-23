file = open('przyklad2.txt', 'r')
rows = file.readlines()

password = ''
for row in rows:
    row = row.strip()
    wordFirst = row + row[0]

    if wordFirst == wordFirst[::-1]:
        password += wordFirst[len(wordFirst)  // 2]

print(password)