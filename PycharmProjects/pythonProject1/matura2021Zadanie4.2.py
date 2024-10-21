file = open('przyklad2.txt', 'r')
rows = file.readlines()

password = ''
index = 0

for i in range(19, len(rows), 20):
    password += rows[i][index]
    index += 1

print(password)