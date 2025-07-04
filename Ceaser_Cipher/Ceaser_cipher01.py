# Encryption
text = input("Enter your message: ")
cipher = ''  # Empty string 
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 2
    if code > ord('Z'):
        code = ord('A')
    cipher = cipher + chr(code)

print(cipher)

## Improved version that includes user specified shifts
text = input("Enter message: ")
shift = 0
while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''
for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char
print(cipher)
