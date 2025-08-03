import random, secrets, string

# Contants
letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation

# concatenate
alphabet = letters + digits + special_char

# Password length 
pwd_length = 12

while True:
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_char for char in pwd) and sum(char in digits for char in pwd)>=2):
        break
    
    print("Simple Output:")
    print(pwd)

