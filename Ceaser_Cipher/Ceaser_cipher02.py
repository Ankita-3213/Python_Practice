# Decryption

cipher = input("Enter crypted message: ")
text = "" # empty string to store decoded text
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 2 # using 2 as we have used 2 in encryption as well
    if code < ord('A'):
        code = ord('Z')
    text = text + chr(code)
print(text)
