def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    money = d.removeprefix('$')
    return float(money)


def percent_to_float(p):
    per = p.removesuffix('%')
    return float("0."+per)



main()
