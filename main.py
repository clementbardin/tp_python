def main():
    while True:
        choice = int(displayMenu())
        if choice == 1:
            requirePayment(3)
        if choice == 2:
            requirePayment(5)
        if choice == 3:
            requirePayment(4.5)
        if choice == 4:
            requirePayment(3)
        if choice == 0:
            break;

        isContinue = input("Do you want to continue? y or n")
        if isContinue == "y":
            print("\n ------------------- \n")
        if isContinue == "n":
            break;

    print("Have a nice day.")


def displayMenu():
    print("1. Café noir | 3 coin")
    print("2. Café au lait | 5 coin")
    print("3. Chocolat au lait | 4.5 coin")
    print("4. Thé | 3 coin")
    print("0. Cancel")
    choice = input("Hello, choose your drink :")
    return int(choice)


def requirePayment(paymentAmount):
    balence = 0;
    while balence < paymentAmount:
        print("You need to pay " + str(paymentAmount - balence) + " coins")
        print("1. 0.5 coin")
        print("2. 1 coin")
        print("3. 2 coins")
        choice = int(input("Please, insert your coins :"))
        if choice == 1:
            balence += 0.5
        if choice == 2:
            balence += 1
        if choice == 3:
            balence += 2

    if balence > paymentAmount:
        print("Here is back your " + str(balence - paymentAmount) + " coin")


main()
