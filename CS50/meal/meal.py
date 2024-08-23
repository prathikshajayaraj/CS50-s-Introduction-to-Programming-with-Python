def main():
    user_input = input("What time is it? ")
    value = convert(user_input)
    if 7.0 <= value <= 8.0:
        print("breakfast time")
    elif 12.0 <= value <= 13.0:
        print("Lunch time")
    elif 18.0 <= value <= 19.0:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    decimal_time = float(hours) + float(minutes) / 60
    return(decimal_time)

if __name__ == "__main__":
    main()

