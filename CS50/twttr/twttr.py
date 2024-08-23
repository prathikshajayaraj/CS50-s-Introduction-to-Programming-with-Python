vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
user_input = input("enter the string ")

for c in user_input:
    if c not in vowels:
        print(c, end="")

