file = open('przyklad2.txt', 'r')
rows = file.readlines()

password = ''
for row in rows :
    row = row.strip()
    number1 = -1

    for char in row :
        if char.isdigit() and number1 == -1 :
            number1 = char
        elif char.isdigit() :
            number2 = char
            asciiCode = number1 + number2

            if 65 <= int(asciiCode) <= 90 :
                letter = chr(int(asciiCode))
                password += letter

        if password.endswith('XXX') :
            break

print(password)
