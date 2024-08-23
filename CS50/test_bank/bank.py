def main():
    user_greeting = input("Greetings received ? ")
    user = value(user_greeting)
    print(f"${user}")


def value(greeting):
    greeting = greeting.casefold().strip()
    if greeting.startswith("hello"):
         return 100
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
