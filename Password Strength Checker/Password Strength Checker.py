password = input("Enter your password: ")

length = len(password) >= 8
uppercase = False
lowercase = False
digit = False
special = False

for char in password:
    if char.isupper():
        uppercase = True
    elif char.islower():
        lowercase = True
    elif char.isdigit():
        digit = True
    else:
        special = True

if length and uppercase and lowercase and digit and special:
    print("Strong Password")
else:
    print("Weak Password")

    if not length:
        print("Password must contain at least 8 characters")
    if not uppercase:
        print("Password must contain an uppercase letter")
    if not lowercase:
        print("Password must contain a lowercase letter")
    if not digit:
        print("Password must contain a digit")
    if not special:
        print("Password must contain a special character")
