file = open('przyklad2.txt', 'r')
rows = file.readlines()

password = ''
for row in rows :
    row = row.strip()
    firstDigit = -1
    secondDigit = -1

    for char in row :
        if char.isdigit() and firstDigit == -1 :
            firstDigit = char
        elif char.isdigit() :
            secondDigit = char
            asciiCode = firstDigit + secondDigit

            if 65 <= int(asciiCode) <= 90 :
                letter = chr(int(asciiCode))
                password += letter

        if password.endswith('XXX') :
            break

print(password)
