def main():
    user_input = input("what will be your input?? ")
    user_output = convert(user_input)
    print(user_output)
def convert(inp):
    return inp.replace(":(","🙁").replace(":)","🙂")


main()
