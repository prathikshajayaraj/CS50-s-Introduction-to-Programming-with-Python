user_greeting = input("Greetings received ? ")
user = user_greeting.casefold().strip()
print(user)
if user.startswith("hello"):
    print("$0")
elif user.startswith("h"):
    print("$20")
else:
    print("$100")

