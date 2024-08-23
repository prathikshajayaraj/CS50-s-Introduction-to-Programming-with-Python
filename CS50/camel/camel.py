user_input = input("CamelCase: ")
user_output = ""
for c in user_input:
    if c.isupper():
        if user_output:
            user_output += "_"
            user_output += c.lower()
    else:
        user_output += c
print("snake_case :" ,user_output)
