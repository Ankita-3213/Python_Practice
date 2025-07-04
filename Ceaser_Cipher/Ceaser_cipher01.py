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
