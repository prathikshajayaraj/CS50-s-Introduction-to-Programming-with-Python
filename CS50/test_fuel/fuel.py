def main():
    try:
      value=convert((input("enter the fuel in fraction x /y? ")))
      print(gauge(value))
    except ValueError:
        print("Error:Invalid input.Both x and y should be numeric or x > y.")
    except ZeroDivisionError:
        print("Error:The y should not be zero.")

def convert(fraction):
    x,y = fraction.split("/")
    if not x.isnumeric() or not y.isnumeric():
        raise  ValueError
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif 1 < percentage < 99:
        return(f"{percentage}%")
    else:
        return("F")


if __name__ == "__main__":
    main()
