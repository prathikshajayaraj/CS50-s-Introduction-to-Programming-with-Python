user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if user_input.strip() == "42" :
    print("yes")
elif user_input.upper() == "FORTY TWO" or user_input.upper() == "FORTY-TWO":
    print("yes")
else:
    print("no")
