Amount_Due = 50
change_owed = 0
valid_coins = [5, 10, 25]
while True:
    coin = int(input("Insert Coin: "))

    if coin in valid_coins:
        if coin <= Amount_Due:
            Amount_Due = Amount_Due - coin
            if Amount_Due != 0:
                print("Amount Due:", Amount_Due)
            else:
                print("Change Owed:", change_owed)
                break
        else:
            change_owed = coin - Amount_Due
            print("Change Owed:", change_owed)
            break
    else:
        print("Amount Due:", Amount_Due)
        break
