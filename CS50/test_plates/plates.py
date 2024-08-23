def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum()):
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if i == 0 or s[i-1].isalpha():  # Check if it's the first digit
                if s[i] == '0':
                    return False
            if not s[i:].isdigit():
                return False
            break

    return True

if __name__ == "__main__":
    main()
