def main():
    output = fuel_tank()
    if output <= 1:
        print("E")
    elif 1 < output < 99:
        print(f"{output}%")
    else:
        print("F")


def fuel_tank():
    while True:
        try:
            x, y = input("enter the fuel in fraction x /y? ").split("/")
            if not x.isnumeric() or not y.isnumeric():
                continue
            x = int(x)
            y = int(y)
            if y == 0 or x > y:
                continue
            else:
                return round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass


main()
