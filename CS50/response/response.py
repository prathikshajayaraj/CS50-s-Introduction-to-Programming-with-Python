from validator_collection import validators,errors
def main():
    user_input =input("What's your email address? ")
    value = email_address(user_input)
    print(value)
def email_address(value):
    try:
        email_address = validators.email(value,allow_empty=False)
        if email_address:
            return("valid")
    except errors.InvalidEmailError:
        return("Invalid")
    except ValueError:
        return ("Invalid")

if __name__=="__main__":
    main()
