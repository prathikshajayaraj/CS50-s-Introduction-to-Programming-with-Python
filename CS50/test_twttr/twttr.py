def main():
    word = input("enter the string: ")
    result= shorten(word)
    print(result)

def shorten(word):
    vowels = "EIOUaeiou"
    result =""
    for c in word:
        if c not in vowels:
           result += c
    return result



if __name__ == "__main__":
    main()


