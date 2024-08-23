def main():
    x, y, z = (input("enter the values ")).split(" ")
    x, z = float(x), float(z)
    output = calculate(x, z, y)
    print(f"{output:.1f}")


def calculate(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    else:
        if b != "0":
            return a / b


main()
